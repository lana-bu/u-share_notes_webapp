import pytest
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token

from api.models import Post


@pytest.mark.django_db
def test_post_list_allows_anonymous_access(api_client, post_factory):
    from datetime import timedelta

    newer = post_factory(title="Newer Notes")
    older = post_factory(title="Older Notes")
    older.created_at = timezone.now() - timedelta(days=1)
    older.save(update_fields=["created_at"])

    response = api_client.get(reverse("post-list"))

    assert response.status_code == status.HTTP_200_OK
    titles = [item["title"] for item in response.data]
    assert titles[0] == newer.title
    assert len(response.data) == 2


@pytest.mark.django_db
def test_post_retrieve_allows_anonymous_access(api_client, post_factory):
    post = post_factory()

    response = api_client.get(reverse("post-detail", args=[post.pk]))

    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == post.pk


@pytest.mark.django_db
def test_post_create_rejects_anonymous_user(api_client, post_payload):
    response = api_client.post(reverse("post-list"), data=post_payload, format="multipart")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_post_create_assigns_authenticated_user(authenticated_client, user, other_user, post_payload):
    response = authenticated_client.post(
        reverse("post-list"),
        data={**post_payload, "user": other_user.pk},
        format="multipart",
    )

    assert response.status_code == status.HTTP_201_CREATED
    created_post = Post.objects.get(pk=response.data["id"])
    assert created_post.user == user
    assert created_post.rating == 0


@pytest.mark.django_db
def test_post_list_supports_filtering(api_client, post_factory):
    post_factory(semester="Winter 2026", instructor_name="Dr. Rivera", title="Match")
    post_factory(semester="Fall 2025", instructor_name="Dr. Smith", title="No Match")

    response = api_client.get(
        reverse("post-list"),
        {"semester": "Winter 2026", "instructor_name": "Dr. Rivera"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert [item["title"] for item in response.data] == ["Match"]


@pytest.mark.django_db
def test_post_list_supports_search(api_client, post_factory):
    post_factory(course_number="CIS 3760", title="Integration Testing", instructor_name="Dr. Rivera")
    post_factory(course_number="MAT 1800", title="Linear Algebra", instructor_name="Dr. Stone")

    response = api_client.get(reverse("post-list"), {"search": "Integration"})

    assert response.status_code == status.HTTP_200_OK
    assert [item["title"] for item in response.data] == ["Integration Testing"]


@pytest.mark.django_db
def test_signup_creates_user(api_client):
    response = api_client.post(
        reverse("signup"),
        {"email": "fresh@example.com", "password": "safe-password-123"},
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {"message": "User account is created successfully."}


@pytest.mark.django_db
def test_signup_rejects_duplicate_email(api_client, user):
    response = api_client.post(
        reverse("signup"),
        {"email": user.email, "password": "safe-password-123"},
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email" in response.data


@pytest.mark.django_db
def test_login_returns_existing_token(api_client, user):
    existing_token = Token.objects.create(user=user)

    response = api_client.post(
        reverse("api-login"),
        {"email": user.email, "password": "safe-password-123"},
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["token"] == existing_token.key
    assert Token.objects.filter(user=user).count() == 1


@pytest.mark.django_db
def test_login_rejects_invalid_credentials(api_client, user):
    response = api_client.post(
        reverse("api-login"),
        {"email": user.email, "password": "wrong-password"},
        format="json",
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.data == {"error": "Invalid username or password"}


@pytest.mark.django_db
def test_logout_deletes_authenticated_users_token(authenticated_client, auth_token):
    response = authenticated_client.post(reverse("logout"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"message": "Successfully logged out."}
    assert not Token.objects.filter(pk=auth_token.pk).exists()


@pytest.mark.django_db
def test_logout_rejects_unauthenticated_user(api_client):
    response = api_client.post(reverse("logout"))

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"error": "You are not logged in."}
