import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker


fake = Faker()

fake_login = fake.user_name()
fake_password = fake.password()

@pytest.fixture()
def page():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://store.steampowered.com/')
    return driver


@pytest.mark.parametrize(
    'user',
    [
        (fake_login, fake_password)
    ]
)
def test_error_message_for_auth(user, page):
    login, password = user

    page.find_element(By.CLASS_NAME, 'global_action_link').click()
    page.find_element(By.XPATH, '//input[@type="text" and not(@id)]').send_keys(login)
    page.find_element(By.XPATH, '//input[@type="password" and not(@id)]').send_keys(password)
    page.find_element(By.XPATH, '//button[@type="submit"]').click()

    error_message = page.find_element(
        By.XPATH,
        '//*[contains(text(), "Пожалуйста, проверьте свой пароль")]'
    ).text

    assert "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова." == error_message

