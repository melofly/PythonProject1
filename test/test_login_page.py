import pytest
from selenium.webdriver.common.by import By
from faker import Faker
from pages.login_page import LoginPage, BasePage

fake = Faker()
fake_login = fake.user_name()
fake_password = fake.password()

@pytest.mark.parametrize(
    'user',
    [
        (fake_login, fake_password)
    ]
)
def test_login_page(user, driver):
    login_page_drive = LoginPage(driver)
    login, password = user
    login_page_drive.login(username=login, password=password)

    error_message = driver.find_element(
        By.XPATH,
        '//*[contains(text(), "Пожалуйста, проверьте свой пароль")]'
    ).text

    assert "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова." == error_message
