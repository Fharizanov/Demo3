"""
The purpose of this automated test case is to show on the screen the team lead profile while logged in as user
"""

from base_test_case import BaseTestCase
import page_selectors
from time import sleep


class TeamLeadProfileTest(BaseTestCase):
    def setUp(self):
        # Opens website demo homepage (http://demo.fluxday.io/users/sign_in)
        self.driver.get('http://demo.fluxday.io/users/sign_in')

    def get_page_element_by_id_and_get_id(self, selector):
        return self.driver.find_element_by_id(selector).get_attribute('id')
    sleep(1)

    def test_fluxday_demo_web_page(self):
        # Checks if there is an email textbox and enters the email of the current user
        self.driver.find_element_by_xpath(page_selectors.xp_expr_email_textbox).send_keys(page_selectors.name)
        self.assertEqual(self.get_page_element_by_id_and_get_id(page_selectors.locator_user_email),
                         page_selectors.locator_user_email, 'Problem with email textbox')

        # Checks if there is a password textbox and enters the password of the current user
        self.driver.find_element_by_xpath(page_selectors.xp_expr_password_textbox).send_keys(page_selectors.password)
        self.assertEqual(self.get_page_element_by_id_and_get_id(page_selectors.locator_user_password),
                         page_selectors.locator_user_password, 'Problem with password textbox')

        # Checks if there is a login button and clicks on it
        self.driver.find_element_by_xpath(page_selectors.xp_expr_login_btn).click()

    def test_user_login(self):
        # Checks if there is a login alert which assures that a login was successful
        login_alert = self.driver.find_element_by_xpath(page_selectors.xp_expr_login_alert)
        self.assertEqual(self.driver.find_element_by_xpath(page_selectors.xp_expr_login_alert), login_alert,
                         'Problem with login alert bottom right')

        # Checks if the logged user is Employee 1
        user = self.driver.find_element_by_xpath(page_selectors.xp_expr_user_name)
        self.assertEqual(self.driver.find_element_by_xpath(page_selectors.xp_expr_user_name), user,
                         'Login user is not the same')

    def test_users_and_lead_profile(self):
        # Clicks on 'Users' button on the left side of the screen
        self.driver.find_element_by_xpath(page_selectors.xp_expr_users_btn).click()
        sleep(1)
        users = self.driver.find_elements_by_xpath(page_selectors.xp_expr_users)
        self.assertNotEqual(len(users), 0, "There are no users")
        self.assertGreater(len(users), 0, "Problem with users counting")

        # Clicks on 'Team Lead' user
        users_number = self.driver.find_elements_by_xpath(page_selectors.xp_expr_users)
        team_lead = self.driver.find_element_by_xpath(page_selectors.xp_expr_lead.
                                                      format(cnt_comments=len(users_number)))
        team_lead.click()
        lead_rights = self.driver.find_element_by_xpath(page_selectors.xp_expr_lead_rights)
        self.assertEqual(lead_rights.text, '#FT2', "Problem with opened profile. Team lead rights do not match.")
        lead_reporting_to = self.driver.find_element_by_xpath(page_selectors.xp_expr_lead_reporting_to)
        self.assertEqual(lead_reporting_to.text, 'Admin User', "Problem with team lead reporting managers."
                                                               " Admin User reference do not match.")
