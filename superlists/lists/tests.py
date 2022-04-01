import imp
from urllib import response
from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)

class HomePageTest(TestCase):
    
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def text_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf-8")
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title> To-Do lists</title>", html)
        self.assertTrue(html.endswith("</html>"))