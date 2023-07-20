from browser import Browser
from pages.login_page import LoginPage
from pages.base_page import BasePage

def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.base_page = BasePage()

def after_all(context):
    context.browser.close()
