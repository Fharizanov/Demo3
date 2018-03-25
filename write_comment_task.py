"""
The purpose of this automated test case is to verify it is possible to write a comment for a task
"""

from base_test_case import BaseTestCase
import page_selectors
from time import sleep


class WriteCommentTasksTest(BaseTestCase):
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

    def test_my_tasks_btn_and_comment(self):
        # Checks if there is a My tasks button and clicks on it
        self.driver.find_element_by_xpath(page_selectors.xp_expr_tasks).click()
        active_pending = self.driver.find_element_by_xpath(page_selectors.xp_expr_pending_btn)
        self.assertEqual('active' in active_pending.get_attribute('class'), True, 'Button Pending is not active')
        sleep(1)
        # Checks if there is a Completed button and clicks on it
        self.driver.find_element_by_xpath(page_selectors.xp_expr_completed_btn).click()
        active_completed = self.driver.find_element_by_xpath(page_selectors.xp_expr_completed_active_btn)
        self.assertEqual('active' in active_completed.get_attribute('class'), True, 'Button Completed is not active')
        # Checks if there are any completed tasks
        completed_tasks = self.driver.find_elements_by_xpath(page_selectors.xp_expr_completed_tasks)
        self.assertNotEqual(len(completed_tasks), 0, 'There are no completed tasks')
        self.assertGreater(len(completed_tasks), 0, 'Problem with completed tasks')
        # Clicks on the first completed task from the top
        self.driver.find_element_by_xpath(page_selectors.xp_expr_first_completed_task).click()
        sleep(1)
        active_first_task = self.driver.find_element_by_xpath(page_selectors.xp_expr_first_completed_task)
        self.assertEqual('active' in active_first_task.get_attribute('class'), True,
                         'Clicking on first task is not active')
        # Click on the number of comments (under 'Add comment' textbox) to show them if any
        self.driver.find_element_by_xpath(page_selectors.xp_expr_comments_num).click()
        sleep(1)
        # Saves the number of comments before submitting new
        comments_before = self.driver.find_elements_by_xpath(page_selectors.xp_expr_comments)
        # Checks if there is a 'Add comment' textbox and enters the desired keys
        self.driver.find_element_by_xpath(page_selectors.xp_expr_comments_textbox).send_keys(page_selectors.comment)
        # Submits the desired keys as a comment
        self.driver.find_element_by_xpath(page_selectors.xp_expr_comments_textbox).submit()
        sleep(1)
        # Verifies that a comment 'Test comment 1" is submited
        comments_number = self.driver.find_elements_by_xpath(page_selectors.xp_expr_comments)
        test_comm = self.driver.find_element_by_xpath(page_selectors.xp_expr_comments_selector.
                                                      format(cnt_comments=len(comments_number)))
        self.assertEqual(test_comm.text, ('emp1 Just now\n' + page_selectors.comment) or
                         ('emp1 1 second ago\n' + page_selectors.comment), 'Submitted comment - different')
        sleep(1)
        # Saves comments number after submitting new
        comments_after = self.driver.find_elements_by_xpath(page_selectors.xp_expr_comments)
        # Verifies that a new comment was submitted
        self.assertEqual(len(comments_after), len(comments_before) + 1, "Problem with counting comments")
