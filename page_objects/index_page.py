from selenium.webdriver.common.by import By


class IndexPage:
    TOP_NAVIGATION = (By.CSS_SELECTOR, '#top')
    LOGO = (By.CSS_SELECTOR, '#logo')
    SEARCH_STRING = (By.CSS_SELECTOR, '[name=search]')
    MENU = (By.CSS_SELECTOR, '#menu')
    CART_BUTTON = (By.CSS_SELECTOR, '#cart > button')
