from page_objects.index_page import IndexPage


def test_index_page_find_elements(browser):
    browser.get(browser.url)
    IndexPage(browser).wait_element(IndexPage.TOP_NAVIGATION)
    IndexPage(browser).wait_element(IndexPage.LOGO)
    IndexPage(browser).wait_element(IndexPage.SEARCH_STRING)
    IndexPage(browser).wait_element(IndexPage.MENU)
    IndexPage(browser).wait_element(IndexPage.CART_BUTTON)


def test_currency_selection(browser):
    browser.get(browser.url)
    IndexPage(browser).choose_euro()
    IndexPage(browser).choose_pound()
    IndexPage(browser).choose_dollar()
