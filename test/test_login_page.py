import pytest
from faker import Faker
from pages.main_page import MainPage
from pages.login_page import LoginPage

fake = Faker()
fake_user = {
    'user':
        (fake.user_name(), fake.password())
}

@pytest.mark.parametrize(
    'login, password',
    [
        (fake_user.get('user'))
    ]
)
def test_login_page(login, password, driver):
    main_page_drive = MainPage(driver=driver)
    main_page_drive.open_login_page()

    login_page_drive = LoginPage(driver=driver)
    login_page_drive.auth(username=login, password=password)

    actual = login_page_drive.get_error_message
    expected = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
    assert actual == expected, f"нам надо это '{expected}',а это хуйня '{actual}'"