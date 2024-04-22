from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def send_keys(self, locator):
        element = self.find_element_with_wait(locator)
        element.send_keys()

    def get_current_url(self):
        return self.driver.current_url

    def drag_and_drop_element(self, source_element, target_element):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def check_element_is_invisible(self, locator):
        WebDriverWait(self.driver, 10).until_not(ec.presence_of_element_located(locator))
        return True

