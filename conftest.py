import pytest
from selenium import webdriver

URL = 'https://store.steampowered.com/'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()
#quit от close отличается тем, что quit закрывает браузер и тем самым убивает сессию драйвера
#close закрывает вкладку, сессия живая, плохой вариант, если работаешь внутри одной вкладки