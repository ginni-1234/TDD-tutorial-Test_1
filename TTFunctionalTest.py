from selenium import webdriver
import unittest
import time
import sys

class WebAppTest(unittest.TestCase):
	def setUp(self):
		# for diff_browser in diff_Browsers:
		# 	print (diff_browser)
		# 	self.browser = diff_browser
		# self.browser = webdriver.Firefox()
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	def test_title_verification(self):
		self.browser.get('https://docs.djangoproject.com/en/1.11/ref/django-admin/')
		
		self.assertIn('Django',self.browser.title)
		time.sleep(5)


if __name__ == '__main__':
	unittest.main()