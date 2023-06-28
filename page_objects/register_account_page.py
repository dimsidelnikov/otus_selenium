from selenium.webdriver.common.by import By


class RegisterAccountPage:
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    CONFIRM_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    PRIVACY_POLICY = (By.LINK_TEXT, 'Privacy Policy')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type=submit]')
    WARNING_PRIVACY_POLICY = (By.CSS_SELECTOR, '.alert')
