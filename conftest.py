import pytest


@pytest.fixture(autouse=True)
def temp_media_root(settings, tmp_path):
    settings.MEDIA_ROOT = tmp_path / "media"
    settings.MEDIA_URL = "/media/"
    return settings.MEDIA_ROOT


@pytest.fixture
def user(db):
    from django.contrib.auth.models import User

    return User.objects.create_user(
        username="student@example.com",
        email="student@example.com",
        password="safe-password-123",
    )


@pytest.fixture
def other_user(db):
    from django.contrib.auth.models import User

    return User.objects.create_user(
        username="other@example.com",
        email="other@example.com",
        password="safe-password-123",
    )


@pytest.fixture
def auth_token(db, user):
    from rest_framework.authtoken.models import Token

    return Token.objects.create(user=user)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def authenticated_client(api_client, auth_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {auth_token.key}")
    return api_client


@pytest.fixture
def uploaded_notes_file():
    from django.core.files.uploadedfile import SimpleUploadedFile

    return SimpleUploadedFile(
        "notes.txt",
        b"These are sample notes.",
        content_type="text/plain",
    )


@pytest.fixture
def post_payload(uploaded_notes_file):
    return {
        "university_name": "Wayne State University",
        "course_number": "CIS 3760",
        "course_name": "Software Engineering II",
        "semester": "Winter 2026",
        "class_section": "001",
        "instructor_name": "Dr. Rivera",
        "lecture_number": 7,
        "date_of_lecture": "2026-03-15",
        "title": "Testing Strategy Notes",
        "description": "Coverage and pytest notes",
        "notes_file": uploaded_notes_file,
    }


@pytest.fixture
def post_factory(db):
    from django.contrib.auth.models import User
    from django.core.files.uploadedfile import SimpleUploadedFile
    from api.models import Post

    def create_post(**overrides):
        user = overrides.pop("user", None) or User.objects.create_user(
            username=f"user-{User.objects.count() + 1}@example.com",
            email=f"user-{User.objects.count() + 1}@example.com",
            password="safe-password-123",
        )
        defaults = {
            "user": user,
            "university_name": "Wayne State University",
            "course_number": "CIS 3760",
            "course_name": "Software Engineering II",
            "semester": "Winter 2026",
            "class_section": "001",
            "instructor_name": "Dr. Rivera",
            "lecture_number": 7,
            "date_of_lecture": "2026-03-15",
            "title": f"Lecture Notes {Post.objects.count() + 1}",
            "description": "Useful notes",
            "notes_file": SimpleUploadedFile(
                f"notes-{Post.objects.count() + 1}.txt",
                b"file contents",
                content_type="text/plain",
            ),
        }
        defaults.update(overrides)
        return Post.objects.create(**defaults)

    return create_post
