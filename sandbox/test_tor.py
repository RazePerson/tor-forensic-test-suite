# import sandbox.consts as consts
import os

import consts as consts

from utils import Utils
from logger import Logging
from system_utils import SystemUtils
from tor_browser_using_stem import TorBrowserUsingStem

log = Logging()
sys = SystemUtils()
utils = Utils()

def wait_until_port_is_open(port):
    log.info("Checking if port % is open..." % port)
    while sys.check_if_port_is_open(port) == 0:
        pass
    log.info("Port % is open" % port)

def launch_and_test_tor(tbb_path, strace_file_tor=None, strace_file_firefox_real=None, strace=False, checkURLs=False):

    tbb = TorBrowserUsingStem(tbb_path=tbb_path)

    tbb.launch_tbb()
    tbb.connect_to_tbb()
    
    pids_tor = os.popen("pgrep tor").read()
    pids_firefox_real = os.popen("pgrep firefox.real").read()
    if strace:
        log.info("Starting strace...")
        sys.strace_on_process_into_file(strace_file_tor, pids_tor)
        sys.strace_on_process_into_file(strace_file_firefox_real, pids_firefox_real)
    
    if checkURLs:
        log.info("Checking URLS...")
        utils.print_urls_from_files(tbb_path, ".*\.bin")

    tbb.load_url(consts.TEST_SITE)
    tbb.kill_process()
    # sys.terminate_processes([pids_tor, pids_firefox_real])

def test_specific_version(version):
    
    tbb_path = utils.download_and_extract_tor_browser(version)
    log.info("Downloaded and extracted Tor into: %s" % tbb_path)
    strace_file_tor = tbb_path + "strace_output_" + version + "_tor"
    strace_file_firefox_real = tbb_path + "strace_output_" + version + "_firefox_real"

    log.info("Launching and testing Tor version %s..." % version)
    tbb_executable_path = tbb_path + "tor-browser_en-US/"
    launch_and_test_tor(tbb_executable_path, checkURLs=True)
    # input("Press enter to delete dir...")
    # sys.delete_dir(tbb_path)

def main():
    # test_specific_version("9.5.1")

    # bin_files = sys.find_files(consts.TBB_PATH, ".*\.bin")
    # for bin_file in bin_files:
    #     found_urls = utils.find_urls_in_file(bin_file)
    #     bin_file_basename = os.path.basename(bin_file)
    #     sys.write_to_file(found_urls, consts.BIN_FILE_URL_PATH + bin_file_basename + "_urls")
        
    # launch_and_test_tor(tbb_path, strace_file_tor, strace_file_firefox_real)
    launch_and_test_tor(consts.TBB_PATH)

if __name__ == '__main__':
    main()