import pytest
from selenium import webdriver

URL = 'https://store.steampowered.com/'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()