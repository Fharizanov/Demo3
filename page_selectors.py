"""
This file contains all xpath expressions, locators and variables that are predefined
"""

xp_expr_logo = '//*[@id="page-top"]/nav/div/div[1]/a/img[1]'
xp_expr_active_demo = '//*[@id="bs-example-navbar-collapse-1"]/ul/li[5]'
xp_expr_demo = '//*[@id="bs-example-navbar-collapse-1"]/ul/li[5]/a'
xp_expr_try_live = '//*[@id="help"]/div/div[2]/div/div[3]/a'
xp_expr_email_textbox = '//*[@id="user_email"]'
xp_expr_login_btn = '//*[@id="new_user"]/div[2]/div[3]/button'
xp_expr_demo_web_page = '//*[@id="new_user"]'
xp_expr_password_textbox = '//*[@id="user_password"]'
xp_expr_login_alert = '/html/body/div[2]/div[1]/div/div'
xp_expr_user_name = '/html/body/div[2]/div[1]/ul[3]/li[1]/a'
xp_expr_tasks = '/html/body/div[2]/div[1]/ul[2]/li[2]/a'
xp_expr_pending_btn = '//*[@id="pane2"]/div[1]/dl/dd[1]'
xp_expr_completed_btn = '//*[@id="pane2"]/div[1]/dl/dd[2]/a'
xp_expr_completed_active_btn = '//*[@id="pane2"]/div[1]/dl/dd[2]'
xp_expr_completed_tasks = '//*[@id="paginator"]/a'
xp_expr_first_completed_task = '//*[@id="paginator"]/a[1]/div'
xp_expr_comments_num = '//*[@id="pane3"]/div[2]/div/div[2]/a'
xp_expr_comments = '//*[@id="pane3"]/div[2]/div/div[2]/div'
xp_expr_comments_selector = '//*[@id="pane3"]/div[2]/div/div[2]/div[{cnt_comments}]'
xp_expr_comments_textbox = '//*[@id="comment_body"]'
xp_expr_users_btn = '/html/body/div[2]/div[1]/ul[2]/li[5]/a'
xp_expr_users = '//*[@id="pane2"]/div[2]/div'
xp_expr_lead = '//*[@id="pane2"]/div[2]/div[{cnt_comments}]/div/div[2]/a[1]'
xp_expr_lead_rights = '//*[@id="pane3"]/div/div[1]/div[1]'
xp_expr_lead_reporting_to = '//*[@id="pane3"]/div/div[1]/div[6]/a'

locator_user_email = 'user_email'
locator_user_password = 'user_password'

name = 'emp1@fluxday.io'
password = 'password'
employee1 = "Employee 1"
comment = 'Test comment 1'
