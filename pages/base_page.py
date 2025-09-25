from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    TIMEOUT = 12

    def __init__(self, driver, timeout=TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)