"""Functions used to handle the driver timeout and exceptions"""

import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from tests import conftest

DEFAULT_WAIT = 30


def wait_for_seconds(seconds_to_wait=5):
    """Hard sleep if absolutely needed. Defaults to 5 seconds"""
    logging.debug(msg=f'Waiting for {seconds_to_wait} seconds...')
    time.sleep(seconds_to_wait)


def get_single_element(driver, findby, identifier, wait_time=DEFAULT_WAIT):
    """
    :rtype: a single selenium webelement
    """
    timeout = conftest.get_timeout_timestamp(wait_time)
    el = None
    try:
        el = driver.find_element(findby, identifier)
        element_logger(findby, identifier, el)
    except NoSuchElementException:
        while bool(el) is False and time.perf_counter() < timeout:
            wait_for_seconds(2)
            logging.debug(msg='Element was not found. Trying to find it again...')
            wait_for_seconds(2)
            try:
                el = driver.find_element(findby, identifier)
                logging.debug(msg=f'We found the element? {bool(el)}')
                if bool(el):
                    el = driver.find_element(findby, identifier)
                    break
            except NoSuchElementException:
                el = False
                logging.debug(msg='Waiting for the element...')
    finally:
        final_logger(el)
    return el


def get_element_list(driver, findby, identifier, wait_time=DEFAULT_WAIT):
    """
    :rtype: a list of selenium webelements
    """
    timeout = conftest.get_timeout_timestamp(wait_time)
    el_list = None
    try:
        el_list = driver.find_elements(findby, identifier)
        element_logger(findby, identifier, el_list)
    except NoSuchElementException:
        while bool(el_list) is False and time.perf_counter() < timeout:
            wait_for_seconds(2)
            logging.debug(msg='Elements were not found. Trying to find them again...')
            wait_for_seconds(2)
            try:
                el_list = driver.find_elements(findby, identifier)
                logging.debug(msg=f'We found the elements? {bool(el_list)}')
                if bool(el_list):
                    el_list = driver.find_elements(findby, identifier)
                    break
            except NoSuchElementException:
                el_list = False
                logging.debug(msg='Waiting for the element...')
    finally:
        final_logger(el_list)
    return el_list


def get_nested_element(driver, findby, element, identifier, wait_time=DEFAULT_WAIT):
    """
    :param driver:
    :rtype: a nested selenium element
    """
    timeout = conftest.get_timeout_timestamp(wait_time)
    el = None
    try:
        el = element.find_element(findby, identifier)
        element_logger(findby, identifier, el)
    except NoSuchElementException:
        while bool(el) is False and time.perf_counter() < timeout:
            wait_for_seconds(2)
            logging.debug(msg='Element was not found. Trying to find it again...')
            wait_for_seconds(2)
            try:
                el = element.find_element(findby, identifier)
                logging.debug(msg=f'We found the element? {bool(el)}')
                if bool(el):
                    el = element.find_element(findby, identifier)
                    break
            except NoSuchElementException:
                el = False
                logging.debug(msg='Waiting for the element...')
    finally:
        final_logger(el)
    return el


def get_nested_elements(driver, findby, element, identifier, wait_time=DEFAULT_WAIT):
    """
    :rtype: a nested selenium element
    """
    timeout = conftest.get_timeout_timestamp(wait_time)
    el_list = None
    try:
        el_list = element.find_elements(findby, identifier)
        element_logger(findby, identifier, el_list)
    except NoSuchElementException:
        while bool(el_list) is False and time.perf_counter() < timeout:
            wait_for_seconds(2)
            logging.debug(msg='Elements were not found. Trying to find them again...')
            try:
                el_list = element.find_elements(findby, identifier)
                logging.debug(msg=f'We found the elements? {bool(el_list)}')
                if bool(el_list):
                    el_list = element.find_elements(findby, identifier)
                    break
            except NoSuchElementException:
                el_list = False
                logging.debug(msg='Waiting for the element...')
    finally:
        final_logger(el_list)
    return el_list


def select_from_dropdown(driver, drpdwn_id, optionparent_id, options_classname, list_option):
    logging.debug(msg=f'Trying to select option: {list_option} for {drpdwn_id}')
    drpdwn = get_single_element(driver, By.ID, drpdwn_id)
    drpdwn.click()
    logging.debug(msg='Checking for dropdown options')
    option_table = get_single_element(driver, By.ID, optionparent_id)
    drpdwn_ops = get_nested_elements(driver, By.CLASS_NAME, option_table, options_classname)
    for item in drpdwn_ops:
        option_text = item.text
        logging.debug(msg=f'There are {len(drpdwn_ops)} options. Option {drpdwn_ops.index(item)}: {option_text}')
        if list_option.lower() == option_text.lower():
            logging.debug(msg=f'Found option: {option_text} for {drpdwn_id}')
            item.click()
            break


def element_logger(findby, identifier: str, element):
    """logging output for the element debug"""
    logging.debug(msg=f'Using {findby} to find identifier {identifier}')
    logging.debug(msg=f'Does the element exist right now? {bool(element)}')


def final_logger(element):
    """logging output for the final clause debug"""
    logging.debug(msg=f'Element found: {bool(element)}')
