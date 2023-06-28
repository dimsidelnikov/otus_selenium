from page_objects.product_card_page import ProductCardPage
from exception_handling import wait_element


def test_product_card_page_find_elements(browser):
    browser.get(browser.url + '/laptop-notebook/macbook')
    wait_element(ProductCardPage.PRODUCT_NAME, browser)
    wait_element(ProductCardPage.ADD_WISH_LIST_BUTTON, browser)
    wait_element(ProductCardPage.COST, browser)
    wait_element(ProductCardPage.QUANTITY_INPUT, browser)
    wait_element(ProductCardPage.ADD_CART_BUTTON, browser)
