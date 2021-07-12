"""To set up the appium driver by Platform Type"""
import logging

"""Created December 15th, 2020 by Alysha Kester-Terry """
import os

from appium import webdriver
from appium.webdriver.appium_service import AppiumService

appium_service = AppiumService()


def get_app_type(PlatformType):
    """To Define the platform type for your app"""
    switcher = {
        PlatformType.ios: 'iOS',
        PlatformType.android: 'Android'
    }
    app_type = switcher.get(PlatformType, 'Invalid environment option, or not yet implemented')
    return app_type


def get_desired_caps(PlatformType, is_headless=False, app_path=None, device_name='iPhone 11', platform_version='14.3'):
    """To Define the desired capabilities type for your app
    :param platform_version:
    :param PlatformType: iOS or Android
    :param is_headless: whether to run headless
    :param app_path: explicit path of app file
    :param device_name: iPhone name or Android emulator name
    """
    platform_type = get_app_type(PlatformType)
    lower_app_type = platform_type.lower()
    if app_path is None:
        app_path = get_app_path(PlatformType)
        logging.info(msg='\nThe App Path we found: {}'.format(app_path))
    desired_caps = None
    if lower_app_type == 'ios':
        if platform_version is None:
            platform_version='14.3'
        if device_name is None:
            device_name='iPhone 11'
        desired_caps = dict(
            platformName='iOS',
            platformVersion=platform_version,
            deviceName=device_name,
            automationName='XCUITest',
            sendKeyStrategy='grouped',
            app=app_path,
            elementResponseAttributes=True,
            isAutomationEnabled=True,
            autoAcceptAlerts=False,
            autoDismissAlerts=False,
            connectHardwareKeyboard=True,
            isHeadless=bool(is_headless),
            showXcodeLog=True
        )
    elif lower_app_type == 'android':
        if device_name is None:
            device_name = 'S7 Edge API 29'
        avd_name = device_name.replace(' ', '_')
        desired_caps = dict(
            platformName='Android',
            deviceName=device_name,
            avd=avd_name,
            automationName='UIAutomator2',
            autoGrantPermissions=False,
            skipDeviceInitialization=False,
            audioPlayback=False,
            skipLogcatCapture=False,
            app=app_path,
            isHeadless=bool(is_headless)
        )
    logging.info(msg='DESIRED CAPABILITIES: {}'.format(desired_caps))
    return desired_caps


def __start_service():
    appium_service.start()
    logging.info(msg='Appium is running? {}'.format(appium_service.is_running))
    logging.info(msg='Appium is listening? {}'.format(appium_service.is_listening))


def get_driver(desired_caps):
    running = appium_service.is_running
    listening = appium_service.is_listening
    logging.info(msg='Appium is running? {}'.format(running))
    logging.info(msg='Appium is listening? {}'.format(listening))
    if running or listening is False:
        __start_service()
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                              desired_capabilities=desired_caps)
    return driver


def get_app_path(PlatformType):
    global file_path
    platform_type = get_app_type(PlatformType)
    logging.info(msg='The App Type is ... {}'.format(platform_type.lower()))
    lower_platform_name = platform_type.lower()
    logging.info(msg='\n Getting a dynamic app path')
    directory_path = os.path.abspath("temp_app_files")
    for root, dirs, files in os.walk(directory_path):
        logging.info(msg=files)
        for file in files:
            logging.info(msg='This file is: {}'.format(file))
            if 'ios' in lower_platform_name.lower():
                if file.endswith('.zip') or file.endswith('.app'):
                    file_path = directory_path + '/' + file
                    logging.info(msg='Found file: {}'.format(file_path))
                    break
            else:
                if file.endswith('.apk'):
                    file_path = directory_path + '/' + file
                    logging.info(msg='Found file: {}'.format(file_path))
                    break
        return os.path.abspath(file_path)


def tear_down():
    appium_service.stop()
    logging.info(msg='Appium is running? {}'.format(appium_service.is_running))
    logging.info(msg='Appium is listening? {}'.format(appium_service.is_listening))
