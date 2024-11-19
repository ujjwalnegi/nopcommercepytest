import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_maker

class Test_01_Login_Admin:
    admin_page_url = Read_Config.get_admin_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_maker.log_gen()

    @pytest.mark.sanity
    def test_title_verification(self, setup):  # testcasemethod
        self.logger.info("********************Test_01_Login_Admin*******************")
        self.logger.info("******************** verification of admin login page title *******************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        expected_title = "Test Login | Practice Test Automation"
        if actual_title == expected_title:
            self.logger.info("******************** test_title_verification matched *******************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("******************** test_title_verification matched not matched*******************")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_valid_login(self, setup):
        self.logger.info("******************** test_valid_login started *******************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_submit_button()
        actual_loginpage_text = self.driver.find_element(By.XPATH,
                                                         "//h1[normalize-space()='Logged In Successfully']").text
        if actual_loginpage_text == "Logged In Successfully":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_submit_button()
        error_msg = self.driver.find_element(By.XPATH, "//div[normalize-space()='Your username is invalid!']").text
        if error_msg == "Your username is invalid!":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
            self.driver.close()
            assert False
