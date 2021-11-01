from logger import Logging
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

import tbselenium.common as cm
import consts as consts

class TorBrowserUsingStem:
    
    def __init__(self):
        self.log = Logging()

    def launch_tbb(self):
        self.log.info("Starting TBB...")
        self.tor_process = launch_tbb_tor_with_stem(tbb_path=consts.TBB_PATH)
        # return self.tor_process.pid

    def connect_to_tbb(self):
        self.log.info("Connecting to TBB...")
        # tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_path)
        self.driver = TorBrowserDriver(consts.TBB_PATH, tor_cfg=cm.USE_STEM, executable_path=consts.GECKODRIVER)
        # input("Press Enter to continue...")
        # self.driver = driver
        
    def load_url(self, url):
        self.driver.load_url(url)

    def kill_process(self):
        self.tor_process.kill()