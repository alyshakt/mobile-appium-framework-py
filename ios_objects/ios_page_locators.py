"""Created December 29th, 2020 by Alysha Kester-Terry
    This Base Page object locator strategy was gleaned with much gratitude from 
    http://elementalselenium.com/tips/9-use-a-base-page-object
"""


class BasePageLocators(object):
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    def __init__(self, driver):
        self.driver = driver

    def alert_type_box(self):
        return self.driver.find_element_by_class_name("XCUIElementTypeAlert")

    def alert_box(self):
        return self.driver.find_element_by_class_name("XCUIElementTypeScrollView")


class IosMemberListPageLocators(BasePageLocators):
    """iOS Member List Page Locators"""

    def member_list_page_title(self):
        return self.driver.find_element_by_name('D+D Members')

    def member_list(self):
        return self.driver.find_elements_by_name('Picture')


class IosMemberDetailPageLocators(BasePageLocators):
    """iOS Member Detail Page Locators"""

    def phone_number(self):
        return self.driver.find_element_by_name('Phone')

    def profile_image(self):
        return self.driver.find_element_by_name('Profile image')

    def email(self):
        return self.driver.find_element_by_name('Email')

    def bio(self):
        return self.driver.find_element_by_name('Bio')
