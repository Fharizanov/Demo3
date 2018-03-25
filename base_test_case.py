"""
All automated tests inherit from this
"""

from unittest import TestCase
from selenium import webdriver


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
