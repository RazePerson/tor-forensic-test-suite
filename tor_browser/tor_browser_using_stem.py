from datetime import datetime
from log.logger import Logging
from selenium.webdriver.common.by import By
from utils.system_utils import SystemUtils
from selenium.webdriver.common.keys import Keys
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

import consts as consts
import tbselenium.common as cm

sys = SystemUtils()


class TorBrowserUsingStem:

    def __init__(self,
                 tbb_path,
                 tor_binary="start-tor-browser",
                 executable_path=consts.DEFAULT_GECKODRIVER_EXECUTABLE,
                 use_custom_profile=True,
                 tbb_profile_path=consts.DEFAULT_TBB_PROFILE_PATH):
        self.tbb_path = tbb_path
        self.tor_binary = tor_binary
        self.executable_path = executable_path
        self.use_custom_profile = use_custom_profile
        self.tbb_profile_path = tbb_profile_path
        self.log = Logging()

    def launch_tbb(self):
        if self.use_custom_profile:
            self.log.info("Launching TBB using custom profile...")
            self.log.info("Checking custom profile path %s" %
                          self.tbb_profile_path)
            if sys.dir_exists(self.tbb_profile_path):
                sys.delete_dir(self.tbb_profile_path)
            sys.create_dir(self.tbb_profile_path)
        else:
            self.log.info("Launching TBB...")
        tor_binary = self.tbb_path + "/" + self.tor_binary
        self.log.info("TBB path: %s" % self.tbb_path)
        self.log.info("Starting TBB: %s" % tor_binary)
        self.tor_process = launch_tbb_tor_with_stem(tbb_path=self.tbb_path)

    def connect_to_tbb(self):
        self.driver = TorBrowserDriver(tbb_path=self.tbb_path,
                                       tor_cfg=cm.USE_STEM,
                                       executable_path=self.executable_path,
                                       use_custom_profile=self.use_custom_profile,
                                       tbb_profile_path=self.tbb_profile_path,
                                       tbb_logfile_path=consts.DEV_NULL)

    def load_url(self, url):
        self.log.info("Loading url: %s" % url)
        self.driver.get(url)

    def search_for_keyword(self, website, search_box_xpath, keyword):
        self.load_url(website)

        search_box = self.driver.find_element(
            by=By.XPATH, value=search_box_xpath)

        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)

    def new_tab(self):
        self.driver.execute_script("window.open('about:blank','secondtab');")

        self.driver.switch_to.window("secondtab")

    def kill_process(self):
        self.log.info("Killing tor process...")
        self.driver.quit()
        tor_pid = sys.get_pid("tor")
        sys.terminate_processes([tor_pid])
        self.termination_time = datetime.now().timestamp()

    def element_exists(self, by, value):
        try:
            self.driver.find_element(by=by, value=value)
        except Exception:
            return False
        return True
