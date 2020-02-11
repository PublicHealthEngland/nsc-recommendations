import pytest
from model_bakery import baker

from nsc.policy.models import Policy
from nsc.utils.markdown import convert


# All tests require the database
pytestmark = pytest.mark.django_db


def test_edit_view(django_app):
    """
    Test that we edit an instance.
    """
    instance = baker.make(Policy)
    response = django_app.get(instance.get_edit_url())
    assert response.context["policy"] == instance


def test_back_link(django_app):
    """
    Test the back link returns to the detail page.
    """
    instance = baker.make(Policy)
    edit_page = django_app.get(instance.get_admin_url()).click(linkid="edit-link-id")
    next_page = edit_page.click(linkid="back-link-id")
    assert next_page.request.path == instance.get_admin_url()


def test_preview_page(django_app):
    """
    Test the preview page.

    The preview page is just the edit page redisplayed with the updated
    values rendered in the same form as the details page and the form
    fields are hidden.
    """
    instance = baker.make(Policy, condition="# heading", next_review=None)

    edit_page = django_app.get(instance.get_edit_url())
    edit_form = edit_page.form
    edit_form["next_review"] = "2020"
    edit_form["condition"] = "# updated"

    preview_page = edit_form.submit(name="preview")
    preview_form = preview_page.form
    assert preview_form["next_review"].attrs["type"] == "hidden"
    assert preview_form["next_review"].value == "2020"
    assert preview_form["condition"].attrs["type"] == "hidden"
    assert preview_form["condition"].value == "# updated"
    assert preview_page.context.get("preview") == "preview"
    assert preview_page.context.get("publish") is None


def test_changes_are_published(django_app):
    """
    Test the policy is updated when the changes are published.
    """
    instance = baker.make(Policy, condition="# heading", next_review=None)

    edit_page = django_app.get(instance.get_edit_url())
    edit_form = edit_page.form
    edit_form["next_review"] = "2020"
    edit_form["condition"] = "# updated"

    preview_page = edit_form.submit(name="preview")

    instance.refresh_from_db()
    assert instance.condition == "# heading"

    preview_form = preview_page.form
    preview_form.submit(name="publish")

    instance.refresh_from_db()
    assert instance.condition == "# updated"
    assert instance.condition_html == convert("# updated")
