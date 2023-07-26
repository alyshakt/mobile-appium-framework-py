"""Created December 15th, 2020 by Alysha Kester-Terry """

import datetime
import logging

import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ios_objects import ios_page_locators
from setup_helpers import driver_setup
from tests import conftest

created_date = str(datetime.datetime.utcnow().strftime("%m-%d-%H%M"))
file_name = 'test-reports/screenshots/ios/' + created_date
default_wait = 15


class BasePage(object):
    """Base class to initialize the page class that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    # Functional/Interaction with Page Elements

    def take_screenshot(self, name=None):
        """Takes a screenshot and saves it to test-reports"""
        if name is None:
            name = 'screenshot'
        screenshot = self.driver.get_screenshot_as_png()
        screenshot_file = open(file_name + name + '.png', "wb")
        screenshot_file.write(screenshot)
        screenshot_file.close()

    def enter_text(self, element, text_to_enter):
        element.clear()
        element.send_keys(text_to_enter)

    def get_element_text(self, element):
        return element.text

    def tap_element(self, element):
        element.click()
        self.wait_for_seconds(2)

    def wait_for_seconds(self, seconds=3):
        conftest.max_sleep(seconds)

    def wait_for_element(self, element):
        try:
            logging.debug(msg='Waiting for element...')
            WebDriverWait(driver=self.driver,
                          timeout=default_wait,
                          poll_frequency=2).until(
                expected_conditions.visibility_of(element))
            logging.debug(msg='The element is found? {}'.format(element.is_displayed()))
        except NoSuchElementException as n:
            logging.debug(msg='Element was not found: {}'.format(element))
        exists = self.element_exists(element)
        logging.debug(msg='The element exists? {}'.format(exists))
        assert exists

    def wait_for_invisibility(self, element):
        logging.debug(msg='Waiting for invisibility of element...')
        WebDriverWait(driver=self.driver,
                      timeout=default_wait,
                      poll_frequency=2).until(
            expected_conditions.invisibility_of_element(element))
        exists = self.element_exists(element)
        logging.debug(msg='The element exists? {}'.format(exists))
        assert exists is False

    def element_exists(self, element):
        return element.is_displayed()

    def swipe_up(self):
        logging.debug(msg='Trying to swipe up!')
        actions = TouchAction(self.driver)
        actions.long_press(x=180, y=510).move_to(x=150, y=250).release().perform()

    def get_page_src_info(self):
        source_hierarchy = self.driver.page_source
        logging.debug(msg=source_hierarchy)

    def process_failure(self, error):
        self.get_page_src_info()
        pytest.fail('The test failed. {}'.format(error), True)

    def tear_down(self, failure):
        if failure is None:
            self.take_screenshot('Pass')
        else:
            self.take_screenshot('Failed')
        self.driver.quit()
        driver_setup.tear_down()


class IosMemberListPage(BasePage):
    """Member List Page Action Methods"""

    def wait_for_load_complete(self):
        self.wait_for_seconds(2)
        title = self.member_list_title_exists()
        self.take_screenshot('MemberListScreen')
        while title is False:
            logging.debug(msg='List page is initiated? {}'.format(title) + ' waiting...')
            self.wait_for_seconds(1)
        logging.debug(msg='is page is initiated? {}'.format(title))

    def member_list_title_exists(self):
        element = ios_page_locators.IosMemberListPageLocators.member_list_page_title(self)
        return self.element_exists(element)

    def get_member_list_title(self):
        element = ios_page_locators.IosMemberListPageLocators.member_list_page_title(self)
        return self.get_element_text(element)

    def tap_member_name(self, member_name):
        member_element_list = ios_page_locators.IosMemberListPageLocators.member_list(self)
        for member_element in member_element_list:
            this_member = self.get_element_text(member_element).lower()
            if member_name.lower() in this_member:
                logging.info(msg='Found member: {}'.format(this_member))
                self.tap_element(member_element)
                break


class IosMemberDetailPage(BasePage):
    """Member Detail Page Action Methods"""

    def wait_for_load_complete(self):
        initiated = self.member_bio_exists()
        logging.debug(msg='Member detail page is initiated? {}'.format(initiated))
        self.take_screenshot('MemberDetailScreen')

    def member_picture_exists(self):
        element = ios_page_locators.IosMemberDetailPageLocators.profile_image(self)
        return self.element_exists(element)

    def member_bio_exists(self):
        element = ios_page_locators.IosMemberDetailPageLocators.bio(self)
        return self.element_exists(element)

    def get_member_bio(self):
        element = ios_page_locators.IosMemberDetailPageLocators.bio(self)
        return self.get_element_text(element)
