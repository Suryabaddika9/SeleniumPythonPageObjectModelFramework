import time
from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from Tests.BaseTest import BaseTest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class TestLogin(BaseTest):
    driver = None
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_my_account_dropdown()
        login_page.enter_login_details("surya1234@gmail.com","Surya690@")
        assert login_page.verify_login_message_is_displayed()

    def test_login_with_invalid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_my_account_dropdown()
        login_page.enter_login_details(self.timestamp_email_generator(), "Surya690@")
        assert login_page.verify_invalid_credentials_warning_message("Warning: No match for E-Mail Address and/or Password.")




