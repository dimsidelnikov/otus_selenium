import random

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from helpers import random_string


class AdminPage(BasePage):
    MENU_CATALOG = (By.CSS_SELECTOR, '#menu-catalog')
    PAGE_PRODUCTS = (By.XPATH, '//*[@id="collapse1"]/li[2]/a')
    ADD_NEW_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, '#input-name1')
    META_TITLE_INPUT = (By.CSS_SELECTOR, '#input-meta-title1')
    DATA_TAB = (By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')
    MODEL_INPUT = (By.CSS_SELECTOR, '#input-model')
    SAVE_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button')
    ALERT_SUCCESS = (By.XPATH, "//div[contains(text(), 'Success: You have modified products!')]")
    CHECKBOX_PRODUCT = (By.CSS_SELECTOR, 'input[type=checkbox]')
    DELETE_PRODUCT_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]')

    def move_to_page_products(self):
        self.click(self.wait_element(self.MENU_CATALOG))
        self.click(self.wait_element(self.PAGE_PRODUCTS))

    def move_to_new_product(self):
        self.click(self.wait_element(self.ADD_NEW_BUTTON))

    def input_new_product_info(self):
        self.input(self.wait_element(self.PRODUCT_NAME_INPUT), random_string())
        self.input(self.wait_element(self.META_TITLE_INPUT), random_string())
        self.click(self.wait_element(self.DATA_TAB))
        self.input(self.wait_element(self.MODEL_INPUT), random_string())

    def save_new_product(self):
        self.click(self.wait_element(self.SAVE_BUTTON))
        self.assert_success()

    def assert_success(self):
        self.wait_element(self.ALERT_SUCCESS)

    def selection_product(self):
        product = self.wait_elements(self.CHECKBOX_PRODUCT)
        self.click(product[random.randint(1, len(product))])

    def delete_product(self):
        self.click(self.wait_element(self.DELETE_PRODUCT_BUTTON))
        self.driver.switch_to.alert.accept()
        self.assert_success()
