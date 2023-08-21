from selenium.webdriver.common.by import By


class LoginAdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type=submit]')
    LOGO = (By.CSS_SELECTOR, 'img[title=OpenCart]')
