# import sandbox.consts as consts
import os
import subprocess
import consts as consts

from time import sleep
from utils import Utils
from logger import Logging
from system_utils import SystemUtils
from tor_browser_using_stem import TorBrowserUsingStem
from tor_browser_using_running_tor import TorBrowserUsingRunningTor

log = Logging()
sys = SystemUtils()
utils = Utils()

def wait_until_port_is_open(port):
    log.info("Checking if port % is open..." % port)
    while sys.check_if_port_is_open(port) == 0:
        pass
    log.info("Port % is open" % port)

def print_urls_that_bin_file(tbb_path):
    file_paths = sys.find_files(tbb_path, ".*scriptCache-child-current\.bin")
    file_strings = ""
    for file in file_paths:
        file_strings = sys.strings(file)
    
    urls = utils.find_url(file_strings)
    excluded_urls = ""
    # print("Found urls:")
    # found_urls = ''.join(utils.exclude_from_list(urls, consts.EXCLUDED_URLS))
    found_urls = ''.join(urls)
    sys.write_to_file(found_urls, tbb_path + "urls_in_bin_file")

def launch_and_test_tor(tbb_path, strace_file_tor=None, strace_file_firefox_real=None, strace=False, checkURLs=False):

    tbb = TorBrowserUsingStem()

    tbb.launch_tbb(tbb_path)
    driver = tbb.connect_to_tbb(tbb_path)
    
    if strace:
        log.info("Starting strace...")
        pids = os.popen("pgrep tor").read()
        sys.strace_on_process_into_file(strace_file_tor, pids)
        pids = os.popen("pgrep firefox.real").read()
        sys.strace_on_process_into_file(strace_file_firefox_real, pids)
    
    if checkURLs:
        log.info("Checking URLS...")
        print_urls_that_bin_file(tbb_path)

    tbb.load_url(consts.TEST_SITE)
    tbb.kill_process()

def test_specific_version(version):
    
    tbb_path = utils.download_and_extract_tor_browser(version)
    log.info("Downloaded and extracted Tor into: %s" % tbb_path)
    strace_file_tor = tbb_path + "strace_output_" + version + "_tor"
    strace_file_firefox_real = tbb_path + "strace_output_" + version + "_firefox_real"

    log.info("Launching and testing Tor version %s..." % version)
    launch_and_test_tor(tbb_path, checkURLs=True)

def main():
    bin_files = sys.find_files(consts.TBB_PATH, ".*\.bin")
    for bin_file in bin_files:
        found_urls = utils.find_urls_in_file(bin_file)
        bin_file_basename = os.path.basename(bin_file)
        sys.write_to_file(found_urls, consts.BIN_FILE_URL_PATH + bin_file_basename + "_urls")
        
    # launch_and_test_tor(tbb_path, strace_file_tor, strace_file_firefox_real)
    # launch_and_test_tor(consts.TBB_PATH, consts.STRACE_FILE_TOR, consts.STRACE_FILE_FIREFOX_REAL)

if __name__ == '__main__':
    main()