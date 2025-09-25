import pytest
from faker import Faker
from pages.login_page import LoginPage

fake = Faker()
fake_login = fake.user_name()
fake_password = fake.password()

@pytest.mark.parametrize(
    'login, password',
    [
        (fake_login, fake_password)
    ]
)
def test_login_page(login, password, driver):
    login_page_drive = LoginPage(driver)
    login_page_drive.login(username=login, password=password)

    el = login_page_drive.error_message_find

    expected = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
    actual = el.text
    assert actual == expected, f"нам надо '{expected}',хуйня '{actual}'"