from behave import *


@given("I am on the login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when("I introduce an unregistred email in the email field")
def step_impl(context):
    # context.login_page.set_email()
    context.login_page.set_email('ceva@gmail.com')
@when("I introduce '{email}' in the email field")
def step_impl(context, email):
    context.login_page.set_email(email)

@when("I introduce the password")
def step_impl(context):
    context.login_page.set_password()


@when("I click on the login button")
def step_impl(context):
    context.login_page.click_login_button()


@then("the main error message is displayed")
def step_impl(context):
    assert context.login_page.is_main_error_message_displayed()


@then('the error message contains "No customer account found"')
def step_impl(context):
    assert "No customer account found" in context.login_page.get_main_error_message()

@when("I introduce an invalid email in the email field")
def step_impl(context):
    context.login_page.set_invalid_email()

@then('the email error message is displayed')
def step_impl(context):
    assert context.login_page.is_email_error_message_displayed()

@then('the error message contains "Wrong email"')
def step_impl(context):
    assert "Wrong email" in context.login_page.get_email_error_message()




