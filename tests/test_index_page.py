from page_objects.index_page import IndexPage
from exception_handling import wait_element


def test_index_page_find_elements(browser):
    browser.get(browser.url)
    wait_element(IndexPage.TOP_NAVIGATION, browser)
    wait_element(IndexPage.LOGO, browser)
    wait_element(IndexPage.SEARCH_STRING, browser)
    wait_element(IndexPage.MENU, browser)
    wait_element(IndexPage.CART_BUTTON, browser)
