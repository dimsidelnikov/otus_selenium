from page_objects.register_account_page import RegisterAccountPage
from exception_handling import wait_element


def test_register_account_page_find_elements(browser):
    browser.get(browser.url + '/index.php?route=account/register')
    wait_element(RegisterAccountPage.FIRSTNAME_INPUT, browser)
    wait_element(RegisterAccountPage.LASTNAME_INPUT, browser)
    wait_element(RegisterAccountPage.EMAIL_INPUT, browser)
    wait_element(RegisterAccountPage.TELEPHONE_INPUT, browser)
    wait_element(RegisterAccountPage.PASSWORD_INPUT, browser)
    wait_element(RegisterAccountPage.CONFIRM_INPUT, browser)
    wait_element(RegisterAccountPage.PRIVACY_POLICY, browser)
    wait_element(RegisterAccountPage.SUBMIT_BUTTON, browser).click()
    wait_element(RegisterAccountPage.WARNING_PRIVACY_POLICY, browser, 0.5)
