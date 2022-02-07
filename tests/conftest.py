"""
conftest.py
"""
import time

from re import search
import pytest
import sandbox.consts as consts

from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from sandbox.tor_browser_using_stem import TorBrowserUsingStem
from selenium.webdriver.support import expected_conditions as EC


from sandbox.logger import Logging
log = Logging()

tbb = {}

def _get_connected_tbb():
    tbb = TorBrowserUsingStem(tbb_path=consts.TBB_PATH)
    tbb.launch_tbb()
    tbb.connect_to_tbb()

    return tbb


@pytest.fixture()
def connected_tbb():
    return _get_connected_tbb()


@pytest.fixture
def timestamp_closed_tbb():
    tbb = _get_connected_tbb()

    timestamp_before = datetime.now().timestamp()

    tbb.kill_process()
    timestamp_after = datetime.now().timestamp()

    timestamp_diff = int(timestamp_after) - int(timestamp_before)
    timestamp = timestamp_after - timestamp_diff

    return timestamp


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
    # self.log.info("Element: " + start_test_button)
    # log.info("Is list: " + str(isinstance(start_test_button, list)))
    # start_test_button = self.driver.find_element(
    #     "/html/body/main/div[2]/a")
    start_test_button.click()

    return tbb


@pytest.fixture
def google_search_tbb():
    tbb = _get_connected_tbb()
    tbb.load_url(consts.GOOGLE)

    # log.info("Looking for cookie button...")
    if tbb.element_exists(by=By.XPATH, value=consts.COOKIE_AGREE_XPATH):
        # log.info("Found it! Clicking it...")
        tbb.driver.find_element(by=By.XPATH, value=consts.COOKIE_AGREE_XPATH).click()
    
    # log.info("Looking for search box element...")
    search_box = tbb.driver.find_element(
        by=By.XPATH, value=consts.GOOGLE_SEARCH_BOX_XPATH)
    # log.info("Found search box element:")
    log.info(search_box)

    # log.info("Searching...")
    search_box.send_keys("Mandalorian")
    # log.info("Pressing return...")
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    # log.info("Done! Killing process...")
    tbb.kill_process()    