from time import sleep
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
test = TestCase()
password = "dummy_pwd"


class SocialAccount:

    def __init__(self, driver):
        self.driver = driver

    def click_on_social_account(self,account_type):
        sleep(3)
        data_list = self.driver.find_elements_by_xpath("//*[@id='content-section']/div/div/div[3]/div/div/div/button/img")
        for data in data_list:
            if data.get_attribute("alt") == account_type:
                data.click()

    def enter_gmail_id(self, gmail_id):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        self.driver.find_element_by_id("identifierId").send_keys(gmail_id)
        self.driver.maximize_window()
        self.click_on_next_button()

    def set_password_as(self):
        self.driver.find_element_by_name("password").send_keys(password)
        self.submit_button()

    def click_on_next_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.ID, "identifierNext")))
        self.driver.find_element_by_id("identifierNext").click()

    def submit_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.ID, "passwordNext")))
        self.driver.find_element_by_id("passwordNext").click()

    def access_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.ID, "submit_approve_access")))
        self.driver.find_element_by_id("submit_approve_access").click()

    def network_page(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located((By.ID, "my-network")))

    def rrc_login_page(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located((By.ID, "Head1")))

    def rrc_email(self, email):
        self.driver.find_element_by_id("L2Content_GenericLogin_LoginSF4_txtUserID").send_keys(email)

    def rrc_password(self, pwd):
        self.driver.find_element_by_id("L2Content_GenericLogin_LoginSF4_txtPassword").send_keys(pwd)

    def rrc_login_button(self):
        self.driver.find_element_by_class_name("submit-Btn").click()

    def rrc_login_error(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located((By.ID, "L2Content_GenericLogin_LoginSF4_lblError")))
        error_msg = self.driver.find_element_by_id("L2Content_GenericLogin_LoginSF4_lblError")
        test.assertEqual(error_msg.text, "Error logging in", "Invalid rrc credential")


