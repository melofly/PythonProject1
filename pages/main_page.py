from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class MainPage(BasePage):
    LOG_BTN = (By.XPATH, "//a[contains(@class, 'global_action_link')]")

    def open_login_page(self):
        self.wait.until(EC.visibility_of_element_located(self.LOG_BTN))
        self.wait.until(EC.element_to_be_clickable(self.LOG_BTN)).click()

