import logging
import time


def pytest_addoption(parser):
    """Defines arguments that can be passed in"""
    parser.addoption("--environment",
                     action="store",
                     default="dev",
                     help="Environment to run tests in")
    parser.addoption("--is_headless",
                     action="store",
                     default=True,
                     help="Whether to run headless")


def pytest_generate_tests(metafunc):
    """Use of the arguments"""
    if 'environment' in metafunc.fixturenames:
        logging.info(msg='\n-----The environment: {}'.format(metafunc.config.option.environment))
        metafunc.parametrize("environment",
                             [str(metafunc.config.option.environment)])
    if 'is_headless' in metafunc.fixturenames:
        logging.info(msg='\n-----Running headless? {}'.format(metafunc.config.option.is_headless))
        metafunc.parametrize("is_headless",
                             [str(metafunc.config.option.is_headless)])


def max_sleep(seconds_to_wait=30):
    """Sleep for seconds"""
    time.sleep(seconds_to_wait)


def get_timeout_timestamp(seconds_to_wait: int = None):
    """ time.perf_counter() returns the current elapsed time of execution including sleep.
    Method returns timeout based on current execution elapsed time."""
    if seconds_to_wait is None:
        seconds_to_wait = max_wait_time_seconds()
    total_wait = time.perf_counter() + seconds_to_wait
    return total_wait


def max_wait_time_seconds(seconds_to_wait=30):
    """For waiting up to x amount of time, for use in while loops"""
    return seconds_to_wait


def pytest_sessionfinish(session, exitstatus):
    """Reports session duration in seconds of the test pass/failure"""
    reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    duration = time.time() - reporter._sessionstarttime
    reporter.write_sep('=',
                       'duration: {} seconds'.format(duration),
                       yellow=True,
                       bold=True)


def pytest_unconfigure(config):
    """Configuration teardown"""
    reporter = config.pluginmanager.get_plugin('terminalreporter')
    duration = time.time() - reporter._sessionstarttime
    reporter.write_sep('=',
                       'duration: {} seconds'.format(duration),
                       yellow=True,
                       bold=True)
