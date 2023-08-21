import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://10.0.2.15:8081/')
    parser.addoption('--maximize', action='store_true')
    parser.addoption('--headless', action='store_true')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    base_url = request.config.getoption('--url')
    maximize = request.config.getoption('--maximize')
    headless = request.config.getoption('--headless')

    if browser_name == 'chrome':
        service = ChromiumService()
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless=new')
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == 'firefox':
        service = FirefoxService()
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(service=service, options=options)
    elif browser_name == 'edge':
        service = EdgeService()
        options = EdgeOptions()
        if headless:
            options.add_argument('--headless=new')
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError(f"Driver {browser_name} is not supported")

    if maximize:
        driver.maximize_window()

    driver.url = base_url

    yield driver

    driver.quit()
