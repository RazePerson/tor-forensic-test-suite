# import sandbox.consts as consts
import os
import subprocess
import consts as consts

from time import sleep
from logger import Logging
from system_utils import SystemUtils
from tor_browser_using_stem import TorBrowserUsingStem
from tor_browser_using_running_tor import TorBrowserUsingRunningTor

log = Logging()
sys = SystemUtils()

def wait_until_port_is_open(port):
    log.info("Checking if port % is open..." % port)
    while sys.check_if_port_is_open(port) == 0:
        pass
    log.info("Port % is open" % port)

def main():

    tbb = TorBrowserUsingStem()

    tbb.launch_tbb()
    # pid = sys.get_pid("\-\-marionette \-no\-remote")
        
    # wait_until_port_is_open(consts.SOCKCS_PORT)
    # sys.check_if_port_is_open(consts.SOCKCS_PORT)
    # sleep(5)
    # sys.check_if_port_is_open(consts.SOCKCS_PORT)
    # wait_until_tbb_port_is_open()
    # start_strace_on_process(tbb_pid, get_username())
    driver = tbb.connect_to_tbb()
    pids = os.popen("pgrep firefox.real").read()
    cmd = "sudo strace -p %s -o %s"%(str(pids), consts.STRACE_FILE)
    log.info("Executing command %s" % cmd)
    os.system(cmd)
    # subprocess.call(["sudo strace -p ", pids, " -o ", consts.STRACE_FILE])
    # log.info("Pids for Tor processes are:")
    # log.info(pids)
    tbb.load_url(consts.TEST_SITE)
    # input("Press Enter to kill Tor process...")
    tbb.kill_process()
    # tor_process.kill()

if __name__ == '__main__':
    main()