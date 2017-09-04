from django.test import TestCase
from django.urls import resolve
from TTapp.views import index
from django.http import HttpRequest
from django.http import HttpResponse

class HomePageTest(TestCase):
# Create your tests here.
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, index)

    # def test_home_page_returned_correct_html(self):
    #     request = HttpRequest()
    #     response = index(request)
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html'))
    #     self.assertIn('<title>To-Do lists</title>',html)
    #     self.assertTrue(html.endswith('</html>'))
