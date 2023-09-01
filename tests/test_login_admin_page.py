from page_objects.login_admin_page import LoginAdminPage
from urllib.parse import urljoin

admin_path = 'admin'


def test_login_admin_page_find_elements(browser):
    browser.get(urljoin(browser.url, admin_path))
    LoginAdminPage(browser).wait_element(LoginAdminPage.USERNAME_INPUT)
    LoginAdminPage(browser).wait_element(LoginAdminPage.PASSWORD_INPUT)
    LoginAdminPage(browser).wait_element(LoginAdminPage.FORGOTTEN_PASSWORD)
    LoginAdminPage(browser).wait_element(LoginAdminPage.SUBMIT_BUTTON)
    LoginAdminPage(browser).wait_element(LoginAdminPage.LOGO)
