from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_element(selector, driver, timeout=1):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(selector))
    except TimeoutException:
        driver.save_screenshot('{}.png'.format(driver.session_id))
        raise AssertionError("didn't wait for the visibility of the element: {}".format(selector))
