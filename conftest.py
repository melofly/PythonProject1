import pytest
from selenium import webdriver

URL = 'https://store.steampowered.com/'
TIMEOUT_ELEMENT = 10

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(TIMEOUT_ELEMENT)
    driver.get(URL)
    yield driver
    driver.quit()