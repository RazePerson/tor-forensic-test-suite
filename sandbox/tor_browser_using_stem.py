from sandbox.logger import Logging
from selenium.webdriver.common.by import By
from sandbox.system_utils import SystemUtils
from selenium.webdriver.common.keys import Keys
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

import sandbox.consts as consts
import tbselenium.common as cm

sys = SystemUtils()


class TorBrowserUsingStem:

    def __init__(self,
                 tbb_path,
                 tor_binary="start-tor-browser",
                 use_custom_profile=True,
                 tbb_profile_path=consts.DEFAULT_TBB_PROFILE_PATH):
        self.tbb_path = tbb_path
        self.tor_binary = tor_binary
        self.use_custom_profile = use_custom_profile
        self.tbb_profile_path = tbb_profile_path
        self.log = Logging()

    def launch_tbb(self):
        if self.use_custom_profile:
            self.log.info("Launching TBB using custom profile...")
            self.log.info("Checking custom profile path %s" %
                          self.tbb_profile_path)
            if not sys.dir_exists(self.tbb_profile_path):
                sys.system_exit("Directory %s doesn't exist!" %
                                self.tbb_profile_path)
        else:
            self.log.info("Launching TBB...")
        tor_binary = self.tbb_path + "/" + self.tor_binary
        self.log.info("TBB path: %s" % self.tbb_path)
        self.log.info("Starting TBB: %s" % tor_binary)
        self.tor_process = launch_tbb_tor_with_stem(tbb_path=self.tbb_path)
        # return self.tor_process.pid

    def connect_to_tbb(self):
        # tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_path)
        self.driver = TorBrowserDriver(tbb_path=self.tbb_path,
                                       tor_cfg=cm.USE_STEM,
                                       executable_path=consts.GECKODRIVER,
                                       use_custom_profile=self.use_custom_profile,
                                       tbb_profile_path=self.tbb_profile_path,
                                       tbb_logfile_path=consts.DEV_NULL)
        # input("Press Enter to continue...")
        # self.driver = driver

    def load_url(self, url):
        self.log.info("Loading url: %s" % url)
        self.driver.get(url)

    def search_for_keyword(self, website, search_box_xpath, keyword):
        self.load_url(website)

        search_box = self.driver.find_element(
            by=By.XPATH, value=search_box_xpath)

        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)

    def kill_process(self):
        self.log.info("Killing tor process...")
        # self.tor_process.kill()
        self.driver.quit()
        tor_pid = sys.get_pid("tor")
        sys.terminate_processes([tor_pid])

    def element_exists(self, by, value):
        try:
            self.driver.find_element(by=by, value=value)
        except Exception:
            return False
        return True
