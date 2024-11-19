from selenium.webdriver.common.by import By


class Login_Admin_Page:
    textbox_username_id = "username"
    textbox_password_id = "password"
    submit_button_id = "submit"
    link_text_logout = "Log out"

    def __init__(self, driver):  # constructor where we are passing driver as a parameter
        self.driver = driver  # using selfdriver we can access the locators

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(By.ID, self.submit_button_id).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_text_logout).click()
