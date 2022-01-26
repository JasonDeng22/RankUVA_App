from django.test import TestCase
from .views import default_map
from django.http import HttpRequest
from django.template import RequestContext
from django.template.loader import render_to_string
from django.test import Client
from django.urls import path


# Create your tests here.

class DummyTestCase(TestCase):
    def setUp(self):
        x = 1

    def test_dummy_test_case(self):
        self.assertEqual(1, 1)


class ViewsTestCase(TestCase):
    def setUp(self):
        client = Client()
        self.response = client.get('')
        # print(self.response)

    def test_render_test_case(self):
        self.assertTemplateUsed(self.response, 'googlelogin/index.html')
