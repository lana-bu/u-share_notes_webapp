import pytest
from django.contrib.auth.models import User

from api.serializers import PostSerializer, UserRegistrationSerializer


@pytest.mark.django_db
def test_post_serializer_accepts_valid_payload(post_payload):
    serializer = PostSerializer(data=post_payload)

    assert serializer.is_valid(), serializer.errors


@pytest.mark.django_db
def test_post_serializer_ignores_read_only_fields(user, post_payload):
    serializer = PostSerializer(
        data={
            **post_payload,
            "user": user.pk,
            "rating": 99,
            "created_at": "2026-03-15T13:00:00Z",
            "updated_at": "2026-03-15T14:00:00Z",
        }
    )

    assert serializer.is_valid(), serializer.errors
    validated = serializer.validated_data
    assert "user" not in validated
    assert "rating" not in validated
    assert "created_at" not in validated
    assert "updated_at" not in validated


@pytest.mark.django_db
def test_user_registration_serializer_creates_user_with_email_as_username():
    serializer = UserRegistrationSerializer(
        data={"email": "newuser@example.com", "password": "safe-password-123"}
    )

    assert serializer.is_valid(), serializer.errors
    user = serializer.save()

    assert user.email == "newuser@example.com"
    assert user.username == "newuser@example.com"
    assert user.check_password("safe-password-123")
    assert serializer.data == {"email": "newuser@example.com"}


@pytest.mark.django_db
def test_user_registration_serializer_rejects_duplicate_email(user):
    serializer = UserRegistrationSerializer(
        data={"email": user.email, "password": "safe-password-123"}
    )

    assert not serializer.is_valid()
    assert "email" in serializer.errors


@pytest.mark.django_db
def test_user_registration_serializer_stores_hashed_password():
    serializer = UserRegistrationSerializer(
        data={"email": "hashed@example.com", "password": "safe-password-123"}
    )
    assert serializer.is_valid(), serializer.errors
    serializer.save()

    created_user = User.objects.get(email="hashed@example.com")
    assert created_user.password != "safe-password-123"
    assert created_user.check_password("safe-password-123")
