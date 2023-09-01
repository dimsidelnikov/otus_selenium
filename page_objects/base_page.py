from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, selector, timeout=1):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(selector))
        except TimeoutException:
            self.driver.save_screenshot('{}.png'.format(self.driver.session_id))
            raise AssertionError("didn't wait for the visibility of the element: {}".format(selector))

    def wait_elements(self, selector, timeout=1):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(selector))
        except TimeoutException:
            self.driver.save_screenshot('{}.png'.format(self.driver.session_id))
            raise AssertionError("didn't wait for the visibility of the elements: {}".format(selector))

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)
