from behave import *
from features.pages.social_account_page import SocialAccount


@when("Login through {social_account}")
def step_impl(context, social_account):
    SocialAccount(context.driver).click_on_social_account(social_account)


@when("Enter valid gmail email id as {gmail_id}")
def step_impl(context, gmail_id):
    SocialAccount(context.driver).enter_gmail_id(gmail_id)


@step("Enter valid gmail password")
def step_impl(context):
    SocialAccount(context.driver).set_password_as()


@step("Click allow access button")
def step_impl(context):
    SocialAccount(context.driver).access_button()


@when("Enter valid gmail invalid email id")
def step_impl(context):
    SocialAccount(context.driver).access_button()


@then("See the RRC login page")
def step_impl(context):
    SocialAccount(context.driver).rrc_login_page()


@when("Enter email id as {email}")
def step_impl(context, email):
    SocialAccount(context.driver).rrc_email(email)


@step("Click on login RRC button")
def step_impl(context):
    SocialAccount(context.driver).rrc_login_button()


@then("I see error page")
def step_impl(context):
    SocialAccount(context.driver).rrc_login_error()


@then("I see network page")
def step_impl(context):
    SocialAccount(context.driver).network_page()


@step("Enter password")
def step_impl(context):
    SocialAccount(context.driver).rrc_password("123444344")
