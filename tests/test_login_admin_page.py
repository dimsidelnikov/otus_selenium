from page_objects.login_admin_page import LoginAdminPage
from exception_handling import wait_element


def test_login_admin_page_find_elements(browser):
    browser.get(browser.url + '/admin')
    wait_element(LoginAdminPage.USERNAME_INPUT, browser)
    wait_element(LoginAdminPage.PASSWORD_INPUT, browser)
    wait_element(LoginAdminPage.FORGOTTEN_PASSWORD, browser)
    wait_element(LoginAdminPage.SUBMIT_BUTTON, browser)
    wait_element(LoginAdminPage.LOGO, browser)
