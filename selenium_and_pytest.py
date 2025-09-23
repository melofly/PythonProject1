import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait


fake = Faker()

fake_login = fake.user_name()
fake_password = fake.password()

@pytest.mark.parametrize(
    'user',
    [
        (fake_login, fake_password)
    ]
)
def test_error_message_for_auth(user):
    login, password = user

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://store.steampowered.com/')
    driver.find_element(By.CLASS_NAME, 'global_action_link').click()
    driver.find_element(By.XPATH, '//input[@type="text" and not(@id)]').send_keys(login)
    driver.find_element(By.XPATH, '//input[@type="password" and not(@id)]').send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    error_message = driver.find_element(
        By.XPATH,
        '//*[contains(text(), "Пожалуйста, проверьте свой пароль")]'
    ).text

    assert "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова." == error_message


