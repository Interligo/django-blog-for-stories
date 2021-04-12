from django.test import TestCase
from django.test import Client
from django.urls import reverse


# TODO: refactor tests

class TestViewsTemplates(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_main_page_template(self) -> None:
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/main_page.html')

    def test_sendemail_page_template(self) -> None:
        response = self.client.get(reverse('sendemail:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sendemail/email.html')

    def test_stories_list_page_template(self) -> None:
        response = self.client.get(reverse('stories:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stories/stories_list.html')

    def test_story_detail_page_template(self) -> None:
        response = self.client.get(reverse('stories:detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stories/story_detail.html')

    def test_about_book_page_template(self) -> None:
        response = self.client.get(reverse('book:about_book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/about_book.html')

    def test_book_content_page_template(self) -> None:
        response = self.client.get(reverse('book:book_content'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_content.html')

    def test_book_chapter_detail_page_template(self) -> None:
        response = self.client.get(reverse('book:chapter_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/chapter_detail.html')
