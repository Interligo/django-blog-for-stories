from django.test import TestCase
from django.urls import reverse
from django.urls import resolve

from main.views import index
from sendemail.views import contact_view


# TODO: refactor tests

class TestUrls(TestCase):
    def test_main_url(self):
        url = reverse('main:index')
        self.assertEqual(resolve(url).func, index)

    def test_contact_url(self):
        url = reverse('sendemail:contact')
        self.assertEqual(resolve(url), contact_view)
