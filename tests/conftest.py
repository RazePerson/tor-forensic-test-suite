"""
conftest.py
"""

import os
import time
import pytest
import consts as consts

from utils.utils import Utils
from log.logger import Logging
from utils.system_utils import SystemUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from tor_browser.tor_browser_using_stem import TorBrowserUsingStem
from selenium.webdriver.support import expected_conditions as EC


log = Logging()
utils = Utils()
sys = SystemUtils()

tbb = {}


def _extract_tbb_path_via_version(tbb_version):
    tbb_path = utils.download_and_extract_tor_browser(tbb_version)
    file_path = sys.find_files(tbb_path, "start-tor-browser*")
    log.info("Found files: " + str(file_path[0]))
    tbb_path = str(os.path.split(str(file_path[0]))[0])
    log.info("Path to binary: " + tbb_path)
    return tbb_path


def _extract_geckodriver_path(tbb_path):
    firefox_version = utils.get_firefox_version_from_tbb_path(tbb_path)
    log.info("Firefox version: %d" % firefox_version)

    gecko_version = utils.find_gecko_version(firefox_version)
    directory = utils.download_and_extract_geckodriver(gecko_version)

    log.info("Geckodriver download directory: " + str(directory))
    log.info("Gecko version: " + str(gecko_version))

    return directory + "geckodriver"


def _get_tbb(tbb_version, tbb_path):
    geckodriver_path = consts.DEFAULT_GECKODRIVER_EXECUTABLE

    if tbb_version != "":
        tbb_path = _extract_tbb_path_via_version(tbb_version)
        geckodriver_path = _extract_geckodriver_path(tbb_path)

    tbb = TorBrowserUsingStem(
        tbb_path=tbb_path, executable_path=geckodriver_path, use_custom_profile=False, tbb_profile_path=tbb_path)
    return tbb


def _get_connected_tbb(tbb_version, tbb_path, manual):

    geckodriver_path = consts.DEFAULT_GECKODRIVER_EXECUTABLE

    if tbb_version != "":
        tbb_path = _extract_tbb_path_via_version(tbb_version)
        geckodriver_path = _extract_geckodriver_path(tbb_path)

    tbb = TorBrowserUsingStem(
        tbb_path=tbb_path, executable_path=geckodriver_path)

    tbb.launch_tbb()
    tbb.connect_to_tbb()

    for url in consts.URLS_TO_LOAD:
        tbb.load_url(url)
        tbb.new_tab()

    tbb.kill_process()

    return tbb


def _check_arguments(tbb_version, tbb_path, manual):

    if tbb_version != "" and tbb_path != consts.TBB_PATH:
        sys.system_exit("Can't use both tbb_version and tbb_path!")

    if tbb_version != "" and manual == True:
        pytest.exit("Manual execution needed for tbb_version %s" % tbb_version)


def pytest_addoption(parser):
    parser.addoption("--tbb_version", action="store", default="")
    parser.addoption("--tbb_path", action="store", default=consts.TBB_PATH)
    parser.addoption("--manual", action="store", default=True)


@pytest.fixture(scope="session")
def connected_tbb(request):
    tbb_version = request.config.option.tbb_version
    tbb_path = request.config.option.tbb_path
    manual = request.config.option.manual
    log.info("version: " + tbb_version)

    _check_arguments(tbb_version, tbb_path, manual)

    if manual == "False":
        tbb = _get_connected_tbb(tbb_version, tbb_path, manual)
    else:
        tbb = _get_tbb(tbb_version, tbb_path)

    yield tbb


@pytest.fixture
def jetstream_tbb():
    tbb = _get_connected_tbb()
    tbb.load_url(consts.JETSTREAM)
    try:
        element_present = EC.presence_of_element_located(
            (By.XPATH, "/html/body/main/div[2]/a"))
        WebDriverWait(tbb.driver, 20).until(element_present)
    except TimeoutException:
        # print("Timed out waiting for page to load")
        tbb.kill_process()
        raise TimeoutException("Timed out waiting for page to load")
    start_test_button = tbb.driver.find_element(by=By.XPATH,
                                                value=consts.JETSTREAM_START_TEST_XPATH)
    start_test_button.click()

    return tbb


@pytest.fixture
def duckduckgo_search_tbb():
    tbb = _get_connected_tbb()
    tbb.load_url(consts.DUCKDUCKGO_ONION)

    search_box = tbb.driver.find_element(
        by=By.XPATH, value=consts.DUCKDUCKGO_SEARCH_BOX_XPATH)
    log.info(search_box)

    search_box.send_keys(consts.DUCKDUCKGO_SEARCH_KEYWORD)
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    tbb.kill_process()
