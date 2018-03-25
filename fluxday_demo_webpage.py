"""
The purpose of this automated test case is to check if it is possible to open fluxday demo web page
"""

from base_test_case import BaseTestCase
import page_selectors
from time import sleep

class FluxdayDemoWebpageTest(BaseTestCase):
    def setUp(self):
        # Opens website homepage (http://fluxday.io)
        self.driver.get('http://fluxday.io')

    def get_page_element_by_id_and_get_id(self, selector):
        return self.driver.find_element_by_id(selector).get_attribute('id')

    def test_logo(self):
        # Checks if the logo of 'http//fluxday.io' is the same
        self.assertEqual(self.driver.find_element_by_xpath(page_selectors.xp_expr_logo),
                         self.driver.find_element_by_xpath(page_selectors.xp_expr_logo), 'Logo is not the same')

    def test_active_demo(self):
        # Click on 'demo' from the top menu
        self.driver.find_element_by_xpath(page_selectors.xp_expr_demo).click()
        sleep(2)
        active_demo = self.driver.find_element_by_xpath(page_selectors.xp_expr_active_demo)
        self.assertEqual(active_demo.get_attribute('class'), 'page-scroll active', 'Button DEMO is not active')

    def test_fluxday_demo_webpage(self):
        # Click on 'Try Live Demo'
        a = self.driver.find_element_by_xpath(page_selectors.xp_expr_try_live)
        # Check if the button exists
        self.assertEqual(a.get_attribute('href'), 'http://demo.fluxday.io/')
        self.driver.get(a.get_attribute('href'))
        # Checks if there is an email textbox
        self.assertEqual(self.get_page_element_by_id_and_get_id(page_selectors.locator_user_email),
                         page_selectors.locator_user_email, 'Problem with email textbox')
        # Checks if there is a password textbox
        self.assertEqual(self.get_page_element_by_id_and_get_id(page_selectors.locator_user_password),
                         page_selectors.locator_user_password, 'Problem with password textbox')
