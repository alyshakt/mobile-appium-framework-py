"""Initializes the webdriver and gets webelements."""
import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import setup_helpers.element_handler as handler
from tests import conftest

DEFAULT_WAIT = 30


def wait_for_seconds(seconds_to_wait=5):
    """Hard sleep if absolutely needed. Defaults to 5 seconds"""
    logging.debug(msg=f'Waiting for {seconds_to_wait} seconds...')
    time.sleep(seconds_to_wait)


class DriverInitialization:
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


class BaseLocators(DriverInitialization):
    """Initializes the driver for use on all other pages and defines objects that are on almost every page.
    The following functions automatically search for an element by a given type of locator, with a wait for visibility
    These methods have 2 different outputs:
    1) The element itself if it is found, or
    2) The boolean value of False if it is not found. This is particularly helpful in asserting that an element exists.

    Each function allows for an explicit max wait time to be passed through as some elements may need extra care for
    loading
    """

    def element_by_name(self, identifier, wait_time=DEFAULT_WAIT):
        findby = By.NAME
        driver = self.driver
        return handler.get_single_element(driver, findby, identifier, wait_time)

    def element_by_id(self, identifier, wait_time=DEFAULT_WAIT):
        findby = By.ID
        driver = self.driver
        return handler.get_single_element(driver, findby, identifier, wait_time)

    def element_by_xpath(self, identifier, wait_time=DEFAULT_WAIT):
        findby = By.XPATH
        driver = self.driver
        return handler.get_single_element(driver, findby, identifier, wait_time)

    def element_by_css(self, identifier, wait_time=DEFAULT_WAIT):
        findby = By.CSS_SELECTOR
        driver = self.driver
        return handler.get_single_element(driver, findby, identifier, wait_time)

    def element_by_classname(self, identifier, wait_time=DEFAULT_WAIT):
        findby = By.CLASS_NAME
        driver = self.driver
        return handler.get_single_element(driver, findby, identifier, wait_time)

    def element_by_xpath_text(self, text_to_find, tag='*', wait_time=DEFAULT_WAIT):
        findby = By.XPATH
        timeout = conftest.get_timeout_timestamp(wait_time)
        el = None
        try:
            el = self.driver.find_element(findby, f'.//{tag}[contains(text(),"{text_to_find}")]')
            logging.debug(msg=f'Using {findby} to find {tag} by containing text {text_to_find}')
            logging.debug(msg=f'Does the element exist right now? {bool(el)}')
        except NoSuchElementException:
            while bool(el) is False and time.perf_counter() < timeout:
                wait_for_seconds(2)
                logging.debug(msg='Element was not found. Trying to find it again...')
                wait_for_seconds(2)
                try:
                    el = self.driver.find_element(findby, f'.//{tag}[contains(text(),"{text_to_find}")]')
                    logging.debug(msg=f'We found the element? {bool(el)}')
                    if bool(el):
                        el = self.driver.find_element(findby, f'.//{tag}[contains(text(),"{text_to_find}")]')
                        break
                except NoSuchElementException:
                    el = False
                    logging.debug(msg='Waiting for the element...')
        finally:
            handler.final_logger(el)
        return el

    def elements_by_name(self, identifier, wait_time=DEFAULT_WAIT):
        findby = By.NAME
        driver = self.driver
        return handler.get_element_list(driver, findby, identifier, wait_time)

    def elements_by_xpath(self, identifier, wait_time=DEFAULT_WAIT):
        findby = By.XPATH
        driver = self.driver
        return handler.get_element_list(driver, findby, identifier, wait_time)

    def elements_by_css(self, identifier, wait_time=DEFAULT_WAIT):
        findby = By.CSS_SELECTOR
        driver = self.driver
        return handler.get_element_list(driver, findby, identifier, wait_time)

    def elements_by_classname(self, identifier, wait_time=DEFAULT_WAIT):
        findby = By.CLASS_NAME
        driver = self.driver
        return handler.get_element_list(driver, findby, identifier, wait_time)

    def elements_by_id(self, identifier, wait_time=DEFAULT_WAIT):
        findby = By.ID
        driver = self.driver
        return handler.get_element_list(driver, findby, identifier, wait_time)

    def elements_by_xpath_text(self, text_to_find, tag='*', wait_time=DEFAULT_WAIT):
        findby = By.XPATH
        timeout = conftest.get_timeout_timestamp(wait_time)
        el_list = None
        try:
            el_list = self.driver.find_elements(findby, f'.//{tag}[contains(text(),"{text_to_find}")]')
            logging.debug(msg=f'Using {findby} to find {tag} by containing text {text_to_find}')
            logging.debug(msg=f'Does the element exist right now? {bool(el_list)}')
        except NoSuchElementException:
            while bool(el_list) is False and time.perf_counter() < timeout:
                wait_for_seconds(2)
                logging.debug(msg='Element was not found. Trying to find it again...')
                wait_for_seconds(2)
                try:
                    el_list = self.driver.find_elements(findby, f'.//{tag}[contains(text(),"{text_to_find}")]')
                    logging.debug(msg=f'Using {findby} to find {tag} by containing text {text_to_find}')
                    logging.debug(msg=f'Does the element exist right now? {bool(el_list)}')
                    break
                except NoSuchElementException:
                    el_list = False
                    logging.debug(msg='Waiting for the element...')
        finally:
            handler.final_logger(el_list)
        return el_list

    def nested_element_by_css(self, element, identifier, wait_time=DEFAULT_WAIT):
        findby = By.CSS_SELECTOR
        driver = self.driver
        return handler.get_nested_element(driver, findby, element, identifier, wait_time)

    def nested_elements_by_css(self, element, identifier, wait_time=DEFAULT_WAIT):
        findby = By.CSS_SELECTOR
        driver = self.driver
        return handler.get_nested_elements(driver, findby, element, identifier, wait_time)

    def nested_element_by_xpath(self, element, identifier, wait_time=DEFAULT_WAIT):
        findby = By.XPATH
        driver = self.driver
        return handler.get_nested_element(driver, findby, element, identifier, wait_time)

    def nested_elements_by_xpath(self, element, identifier, wait_time=DEFAULT_WAIT):
        findby = By.XPATH
        driver = self.driver
        return handler.get_nested_elements(driver, findby, element, identifier, wait_time)

    def nested_element_by_id(self, element, identifier, wait_time=DEFAULT_WAIT):
        findby = By.ID
        driver = self.driver
        return handler.get_nested_element(driver, findby, element, identifier, wait_time)

    def nested_elements_by_id(self, element, identifier, wait_time=DEFAULT_WAIT):
        findby = By.ID
        driver = self.driver
        return handler.get_nested_elements(driver, findby, element, identifier, wait_time)

    def nested_elements_by_classname(self, element, identifier, wait_time=DEFAULT_WAIT):
        findby = By.CLASS_NAME
        driver = self.driver
        return handler.get_nested_elements(driver, findby, element, identifier, wait_time)
