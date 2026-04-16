import pytest

from api.models import Post


@pytest.mark.django_db
def test_post_can_be_created_with_required_fields(user, uploaded_notes_file):
    post = Post.objects.create(
        user=user,
        university_name="Wayne State University",
        course_number="CIS 3760",
        course_name="Software Engineering II",
        semester="Winter 2026",
        class_section="001",
        instructor_name="Dr. Rivera",
        lecture_number=7,
        date_of_lecture="2026-03-15",
        title="Lecture 7 Notes",
        description="Detailed notes",
        notes_file=uploaded_notes_file,
    )

    assert post.pk is not None
    assert post.rating == 0
    assert post.notes_file.name.endswith("notes.txt")


@pytest.mark.django_db
def test_post_string_representation_uses_title_and_course_number(post_factory):
    post = post_factory(title="Midterm Review", course_number="CIS 4000")

    assert str(post) == "Midterm Review - CIS 4000"
