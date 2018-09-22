from behave import *
from features.pages.login_page import LoginPage


@when("Open the Radius url")
def step_impl(context):
    LoginPage(context.driver).radius_url()


@step("Navigate to {tab_name} page")
def step_impl(context, tab_name):
    LoginPage(context.driver).navigate_to_login_page(tab_name)


@when("Enter valid email id as {email_id}")
def step_impl(context,email_id):
    LoginPage(context.driver).email_id(email_id)


@step("Enter valid password")
def step_impl(context):
    LoginPage(context.driver).password("12345678")


@step("Click on login button")
def step_impl(context):
    LoginPage(context.driver).click_on_login_button()


@when("Enter invalid email id as {invalid_id}")
def step_impl(context, invalid_id):
    LoginPage(context.driver).email_id(invalid_id)


@step("Enter invalid password")
def step_impl(context):
    LoginPage(context.driver).password("12er43366")


@then("I see error message")
def step_impl(context):
    LoginPage(context.driver).error_message()


@then("I see validation message")
def step_impl(context):
    LoginPage(context.driver).validation_message()


@when("I click on forget password link")
def step_impl(context):
    LoginPage(context.driver).click_on_forget_password()


@then("I redirect forget password page")
def step_impl(context):
    LoginPage(context.driver).forget_password_page()


@step("Enter email id and click on reset email button")
def step_impl(context):
    LoginPage(context.driver).click_on_resend_email()


@when("Enter email id with invalid domain name as {name}")
def step_impl(context, name):
    LoginPage(context.driver).email_id(name)


@when("Enter email id without @ as {username}")
def step_impl(context,username):
    LoginPage(context.driver).email_id(username)


@when("Enter email id without dot as {user_id}")
def step_impl(context,user_id):
    LoginPage(context.driver).email_id(user_id)


@when("Enter password with space")
def step_impl(context):
    LoginPage(context.driver).password("12345678  ")


@step("Click on logout button")
def step_impl(context):
    LoginPage(context.driver).logout_button()


@then("See the success message")
def step_impl(context):
    LoginPage(context.driver).success_message()


@then("Show error {message}")
def step_impl(context, message):
    LoginPage(context.driver).error_invalid_id(message)


@step("Click on reset button")
def step_impl(context):
    LoginPage(context.driver).resend_button()