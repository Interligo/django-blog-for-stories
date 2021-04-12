from selenium import webdriver
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from stories.models import Story


class TestStoriesList(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.close()

    def test_find_stories_list_link_on_main_page(self) -> None:
        self.browser.get(self.live_server_url)
        stories_list_element = self.browser.find_element_by_id('stories-list')
        self.assertEqual(
            stories_list_element.text,
            'Список рассказов'
        )

    def test_is_button_from_main_page_redirect_to_stories_list_page(self) -> None:
        stories_list_url = self.live_server_url + reverse('stories:index')
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('stories-list').click()
        self.assertEqual(
            self.browser.current_url,
            stories_list_url
        )

    def test_empty_stories_list_page(self) -> None:
        self.browser.get(self.live_server_url + reverse('stories:index'))
        self.assertEqual(
            self.browser.find_element_by_id('content-container').text,
            'Ничего не найдено.'
        )

    def test_is_stories_list_on_screen(self) -> None:
        self.test_story = Story.objects.create(
            story_title='Заголовок',
            story_text='Текст'
        )
        self.browser.get(self.live_server_url + reverse('stories:index'))
        self.assertEqual(
            self.browser.find_element_by_class_name('card-title').text,
            'Заголовок'
        )

    def test_is_button_on_stories_list_page_redirect_to_story_detail(self) -> None:
        detail_url = self.live_server_url + reverse('stories:detail', args=[1])
        self.test_story = Story.objects.create(
            story_title='Заголовок',
            story_text='Текст'
        )
        self.browser.get(self.live_server_url + reverse('stories:index'))
        self.browser.find_element_by_link_text('Перейти к рассказу').click()
        self.assertEqual(
            self.browser.current_url,
            detail_url
        )
