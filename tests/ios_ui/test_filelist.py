"""Created December 15th, 2020 by Alysha Kester-Terry """

from ios_objects import ios_pages
from setup_helpers import driver_setup
from setup_helpers.PlatformType import PlatformType


def test_filelist(is_headless, record_xml_attribute):
    """A basic test to check for a file list"""
    record_xml_attribute(
        "name",
        "The title of the test for XML output")
    platform = PlatformType.ios
    desired_caps = driver_setup.get_desired_caps(PlatformType=platform, is_headless=is_headless)
    # Setup Driver, define Platform Type and the page object
    driver = driver_setup.get_driver(desired_caps)
    # I recommend beginning with a try-catch-finally format
    base_page = ios_pages.BasePage(driver)
    member_list_page = ios_pages.IosMemberListPage(driver)
    member_detail_page = ios_pages.IosMemberDetailPage(driver)
    failed = None
    try:
        member_list_page.wait_for_load_complete()
        assert member_list_page.member_list_title_exists()
        print('The page title is: ' + member_list_page.get_member_list_title())
        member_list_page.tap_member_name('Alysha')
        member_detail_page.wait_for_load_complete()
        assert member_detail_page.member_bio_exists()
        print('The Bio exists and says: {}'.format(member_detail_page.get_member_bio()))
    except (Exception, BaseException) as failure:
        # If any assertions above fail, then mark the test as failed and capture a screenshot
        print('!!!!! The test failed. {}'.format(failure))
        failed = failure
        base_page.process_failure(failed)
    finally:
        # Finally, quit the driver and appium service!
        base_page.tear_down(failed)
