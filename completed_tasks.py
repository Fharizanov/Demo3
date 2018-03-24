from base_test_case import BaseTestCase
import page_selectors


class CompletedTasks(BaseTestCase):
    def setUp(self):
        # Opens website demo homepage (http://demo.fluxday.io/users/sign_in)
        self.driver.get('http://demo.fluxday.io/users/sign_in')

    def get_page_element_by_id_and_get_id(self, selector):
        return self.driver.find_element_by_id(selector).get_attribute('id')

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

    def test_my_tasks_btn(self):
        # Checks if there is a My tasks button and clicks on it
        self.driver.find_element_by_xpath(page_selectors.xp_expr_tasks).click()
        active_pending = self.driver.find_element_by_xpath(page_selectors.xp_expr_pending_btn)
        self.assertNotEqual(active_pending.get_attribute('class'), 'active', 'Button Pending is not active')

    def test_completed_btn(self):
        # Checks if there is a Completed button and clicks on it
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(page_selectors.xp_expr_completed_btn).click()
        active_completed = self.driver.find_element_by_xpath(page_selectors.xp_expr_completed_active_btn)
        self.assertEqual(active_completed.get_attribute('class'), 'active', 'Button Completed is not active')

    def test_completed_tasks(self):
        # Checks if there are any completed tasks
        completed_tasks = self.driver.find_elements_by_xpath(page_selectors.xp_expr_completed_tasks)
        self.assertNotEqual(len(completed_tasks), 0, 'There are no completed tasks')
        self.assertGreater(len(completed_tasks), 0, 'Problem with completed tasks')
        print(len(completed_tasks()))
