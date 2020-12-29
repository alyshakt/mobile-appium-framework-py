"""To set up the appium driver by Platform Type"""
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
    print(switcher.get(PlatformType), 'Invalid app type.')
    return switcher.get(PlatformType)


def get_desired_caps(PlatformType, is_headless=False, app_path=None, device_name=None):
    """To Define the desired capabilities type for your app
    :param PlatformType: iOS or Android
    :param is_headless: whether to run headless
    :param app_path: explicit path of app file
    :param device_name: iPhone name or Android emulator name
    """
    platform_type = get_app_type(PlatformType)
    lower_app_type = platform_type.lower()
    if app_path is None:
        app_path = get_app_path(PlatformType)
        print('\nThe App Path we found: {}'.format(app_path))
    desired_caps = None
    if lower_app_type == 'ios':
        if device_name is None:
            device_name = 'iPhone 11'
        desired_caps = dict(
            platformName='iOS',
            platformVersion='14.1',
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
    print('DESIRED CAPABILITIES: {}'.format(desired_caps))
    return desired_caps


def __start_service():
    appium_service.start()
    print('Appium is running? {}'.format(appium_service.is_running))
    print('Appium is listening? {}'.format(appium_service.is_listening))


def get_driver(desired_caps):
    running = appium_service.is_running
    listening = appium_service.is_listening
    print('Appium is running? {}'.format(running))
    print('Appium is listening? {}'.format(listening))
    if running or listening is False:
        __start_service()
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                              desired_capabilities=desired_caps)
    return driver


def get_app_path(PlatformType):
    global file_path
    platform_type = get_app_type(PlatformType)
    print('The App Type is ... {}'.format(platform_type.lower()))
    lower_platform_name = platform_type.lower()
    print('\n Getting a dynamic app path')
    directory_path = os.path.abspath("temp_app_files")
    for root, dirs, files in os.walk(directory_path):
        print(files)
        for file in files:
            print('This file is: {}'.format(file))
            if 'ios' in lower_platform_name.lower():
                if file.endswith('.zip') or file.endswith('.app'):
                    file_path = directory_path + '/' + file
                    print('Found file: {}'.format(file_path))
                    break
            else:
                if file.endswith('.apk'):
                    file_path = directory_path + '/' + file
                    print('Found file: {}'.format(file_path))
                    break
        return os.path.abspath(file_path)


def tear_down():
    appium_service.stop()
    print('Appium is running? {}'.format(appium_service.is_running))
    print('Appium is listening? {}'.format(appium_service.is_listening))
