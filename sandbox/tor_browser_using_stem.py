from logger import Logging
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

import tbselenium.common as cm
import consts as consts

class TorBrowserUsingStem:
    
    def __init__(self):
        self.log = Logging()

    def launch_tbb(self, tbb_path, tor_binary="start-tor-browser"):
        tor_binary = tbb_path + tor_binary
        self.log.info("TBB path: %s" % tbb_path)
        self.log.info("Starting TBB: %s" % tor_binary)
        self.tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_path)
        # return self.tor_process.pid

    def connect_to_tbb(self, tbb_path):
        self.log.info("Connecting to TBB...")
        # tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_path)
        self.driver = TorBrowserDriver(tbb_path, tor_cfg=cm.USE_STEM, executable_path=consts.GECKODRIVER)
        # input("Press Enter to continue...")
        # self.driver = driver
        
    def load_url(self, url):
        self.log.info("Loading url: %s" % url)
        self.driver.load_url(url)

    def kill_process(self):
        self.tor_process.kill()