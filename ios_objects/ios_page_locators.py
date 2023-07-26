"""Created December 29th, 2020 by Alysha Kester-Terry
    This Base Page object locator strategy was gleaned with much gratitude from 
    http://elementalselenium.com/tips/9-use-a-base-page-object
"""
from setup_helpers.locators_util import BaseLocators


class BasePageLocators:
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    def __init__(self, driver):
        self.driver = driver

    def alert_type_box(self):
        return BaseLocators.element_by_name(self, "XCUIElementTypeAlert")

    def alert_box(self):
        return BaseLocators.element_by_classname(self, "XCUIElementTypeScrollView")


class IosMemberListPageLocators(BasePageLocators):
    """iOS Member List Page Locators"""

    def member_list_page_title(self):
        return BaseLocators.element_by_name(self, 'D+D Members')

    def member_list(self):
        return BaseLocators.elements_by_name(self, 'Picture')


class IosMemberDetailPageLocators(BasePageLocators):
    """iOS Member Detail Page Locators"""

    def phone_number(self):
        return BaseLocators.element_by_name(self, 'Phone')

    def profile_image(self):
        return BaseLocators.element_by_name(self, 'Profile image')

    def email(self):
        return BaseLocators.element_by_name(self, 'Email')

    def bio(self):
        return BaseLocators.element_by_name(self, 'Bio')
