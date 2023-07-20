from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
   LOGIN_PAGE_URL = 'https://demo.nopcommerce.com/login'
   INPUT_EMAIL = (By.ID, "Email")
   INPUT_PASSWORD = (By.ID, "Password")
   BUTTON_LOGIN = (By.CLASS_NAME, "login-button")
   ERROR_MSG_MAIN = (By.CSS_SELECTOR, "div.message-error")
   ERROR_MSG_EMAIL = (By.ID, "Email-error")

   def navigate_to_login_page(self):
      self.browser.get(self.LOGIN_PAGE_URL)

   def set_email(self, email):
      self.type(self.INPUT_EMAIL, email)

   def set_invalid_email(self):
      self.type(self.INPUT_EMAIL, "ceva")

   def set_password(self):
      self.type(self.INPUT_PASSWORD, "123")

   def click_login_button(self):
      self.click(self.BUTTON_LOGIN)

   def is_main_error_message_displayed(self):
      return self.find(self.ERROR_MSG_MAIN).is_displayed()


   def get_main_error_message(self):
      return self.get_text(self.ERROR_MSG_MAIN)


   def is_email_error_message_displayed(self):
      return self.find(self.ERROR_MSG_EMAIL).is_displayed()


   def get_email_error_message(self):
      return self.get_text(self.ERROR_MSG_EMAIL)