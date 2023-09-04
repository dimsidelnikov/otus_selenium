from page_objects.catalog_page import CatalogPage
from urllib.parse import urljoin

laptop_path = 'laptop-notebook'


def test_catalog_page_find_elements(browser):
    browser.get(urljoin(browser.url, laptop_path))
    CatalogPage(browser).wait_element(CatalogPage.CATEGORY_HEADER)
    CatalogPage(browser).wait_element(CatalogPage.LIST_VIEW_BUTTON)
    CatalogPage(browser).wait_element(CatalogPage.GRID_VIEW_BUTTON)
    CatalogPage(browser).wait_element(CatalogPage.SORTING_SELECTION)
    CatalogPage(browser).wait_element(CatalogPage.LIMIT_SELECTION)
