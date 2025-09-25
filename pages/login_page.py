from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class, 'global_action_link')]")
    INPUT_LOGIN = (By.XPATH, '//input[@type="text" and not(@id) and not(@role)]')
    INPUT_PASSWORD = (By.XPATH, '//input[@type="password" and not(@id)]')
    BUTTON_AUTH = (By.XPATH, '//button[@type="submit" and contains(text(), "Войти")]')
    ERROR_MESSAGE_EL =  (By.XPATH, '//button/parent::div/following-sibling::div')

    def login(self, username: str, password: str):
        self.click(self.LOGIN_BUTTON)
        self.input_element(self.INPUT_LOGIN, username)
        self.input_element(self.INPUT_PASSWORD, password)
        self.click(self.BUTTON_AUTH)

    @property
    def error_message_find(self):
        el = self.find_element(self.ERROR_MESSAGE_EL)
        return el


