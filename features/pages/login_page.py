from time import sleep
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
login_url = "https://radiusagent.com/"
test = TestCase()


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def radius_url(self):
        self.driver.get(login_url)
        sleep(5)

    def navigate_to_login_page(self, tab_name):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Header__StyledNavItem-sc-1rogux4-6")))
        menu_list = self.driver.find_elements_by_class_name("Header__StyledNavItem-sc-1rogux4-6")
        for name in menu_list:
            if name.text == tab_name:
                name.click()
                break

    def email_id(self, email_id):
        name = self.driver.find_element_by_xpath("//input[@type='email']")
        name.clear()
        name.send_keys(email_id)

    def password(self, password):
        pwd = self.driver.find_element_by_xpath("//input[@type='password']")
        pwd.clear()
        pwd.send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def error_message(self):
        self.wait_for_invisibility()

    def wait_for_invisibility(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "notification-container-empty")))

    def logout_button(self):
        self.driver.find_element_by_class_name("fa-angle-down").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[ng-click='vm.logout()']")))
        self.driver.find_element_by_css_selector("[ng-click='vm.logout()']").click()

    def validation_message(self):
        error_list = self.driver.find_elements_by_class_name("Input__Error-ibe67n-1")
        test.assertEqual(error_list[0].text, "Email is required.", "Email id is blank")
        test.assertEqual(error_list[1].text, "Password is required.", "Password is blank")

    def click_on_forget_password(self):
        self.driver.find_element_by_class_name("Login__ForgotPassword-l0cx5q-3").click()

    def forget_password_page(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Input__Label-ibe67n-3")))

    def click_on_resend_email(self):
        self.reset_email("shivanit875@gmail.com")
        self.resend_button()

    def resend_button(self):
        self.driver.find_element_by_class_name("Button-sc-12smwpy-0").click()

    def reset_email(self,email):
        self.driver.find_element_by_class_name("TextBox__Input-zfpcai-0").send_keys(email)

    def success_message(self):
        message = self.driver.find_element_by_class_name("CheckEmail__Para-peevyl-1")
        test.assertEqual(message.text, "Check your email for a link to reset your password.", "resend email not working")

    def error_invalid_id(self, message):
        error_msg = self.driver.find_element_by_class_name("Input__Error-ibe67n-1")
        test.assertEqual(error_msg.text, message, "error message is not showing")

