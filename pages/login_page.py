from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    INPUT_LOGIN = (By.XPATH, '//input[@type="text" and not(@id) and not(@role)]')
    INPUT_PASSWORD = (By.XPATH, '//input[@type="password" and not(@id)]')
    BUTTON_AUTH = (By.XPATH, '//button[@type="submit" and contains(text(), "Войти")]')
    ERROR_MESSAGE = (
        By.XPATH,
        "//button[@type='submit']/ancestor::div[1]/following-sibling::div[string-length(.) > 1]"
    )

    def auth(self, username: str, password: str):
        locators_auth = {self.INPUT_LOGIN, self.INPUT_PASSWORD}

        try:
            for locator in locators_auth:
                self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
                print("Не дождался появления одного из обязательных элементов для авторизации")

        self.wait.until(EC.visibility_of_element_located(self.INPUT_LOGIN)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.INPUT_PASSWORD)).send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.BUTTON_AUTH)).click()

    @property
    def get_error_message(self):
        error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error_element.text







