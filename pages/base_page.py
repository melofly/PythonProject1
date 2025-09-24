import enum
from typing import Union

import pytest, selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum
from locators.locators_for_login_page import Locators


class BasePage:
    TIMEOUT_ELEMENT = 10

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=TIMEOUT_ELEMENT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator, timeout=TIMEOUT_ELEMENT):
        self.find_element(locator, timeout).click()

    def input_element(self, locator, text, timeout=TIMEOUT_ELEMENT):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)









