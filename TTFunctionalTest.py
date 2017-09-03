from selenium import webdriver
import unittest
import time
import sys
from selenium.webdriver.common.keys import Keys

class WebAppTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	def test_title_verification(self):
		self.browser.get('https://www.google.com/')
		self.assertIn('Google',self.browser.title)

	def test_input_verification(self):
		self.browser.get('https://www.google.com/')
		elem = self.browser.find_element_by_name('q')
		elem.clear()
		elem.send_keys('Kitty')
		elem.send_keys(Keys.RETURN)
		self.assertIn('Kitty',self.browser.title)
		time.sleep(5)

if __name__ == '__main__':
	unittest.main()