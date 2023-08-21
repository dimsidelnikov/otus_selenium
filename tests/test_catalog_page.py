from page_objects.catalog_page import CatalogPage
from exception_handling import wait_element


def test_catalog_page_find_elements(browser):
    browser.get(browser.url + '/laptop-notebook')
    wait_element(CatalogPage.CATEGORY_HEADER, browser)
    wait_element(CatalogPage.LIST_VIEW_BUTTON, browser)
    wait_element(CatalogPage.GRID_VIEW_BUTTON, browser)
    wait_element(CatalogPage.SORTING_SELECTION, browser)
    wait_element(CatalogPage.LIMIT_SELECTION, browser)
