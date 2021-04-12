from django.test import SimpleTestCase

from stories.forms import LeaveCommentForm


class TestLeaveCommentForm(SimpleTestCase):
    def test_form_with_valid_data(self) -> None:
        form = LeaveCommentForm(data={
            'author': 'comment_author',
            'text': 'comment_text'
        })
        self.assertTrue(form.is_valid())

    def test_form_with_no_data(self) -> None:
        form = LeaveCommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
