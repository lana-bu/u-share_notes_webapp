import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_homepage_renders_posts_in_context(client, post_factory):
    post_factory(title="Homepage Notes")

    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert "home.html" in [template.name for template in response.templates]
    assert list(response.context["posts"])[0].title == "Homepage Notes"


@pytest.mark.parametrize(
    ("route_name", "template_name"),
    [
        ("login", "registration/login.html"),
        ("signup", "registration/signup.html"),
        ("create-post", "create-post.html"),
    ],
)
@pytest.mark.django_db
def test_static_pages_render_expected_templates(client, route_name, template_name):
    response = client.get(reverse(route_name))

    assert response.status_code == 200
    assert "base.html" in [template.name for template in response.templates]
    assert template_name in [template.name for template in response.templates]
