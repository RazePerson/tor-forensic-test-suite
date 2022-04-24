from log.logger import Logging
from tbselenium.tbdriver import TorBrowserDriver

import subprocess
import tbselenium.common as cm
import consts as consts


class TorBrowserUsingRunningTor:

    def __init__(self):
        self.log = Logging()

    def launch_tbb(self):
        self.log.info("Starting TBB...")
        pid = subprocess.Popen("./" + consts.TBB_RUNNABLE,
                               cwd=consts.TBB_PATH).pid
        return pid

    def connect_to_tbb(self):
        self.log.info("Connecting to TBB...")
        # tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_path)
        with TorBrowserDriver(tbb_path=consts.TBB_PATH, tor_cfg=cm.USE_RUNNING_TOR,
                              socks_port=consts.SOCKCS_PORT, executable_path=consts.GECKODRIVER) as driver:
            # input("Press Enter to continue...")
            self.driver = driver

    def load_url(self, url):
        self.driver.load_url(url)
