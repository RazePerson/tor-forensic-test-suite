import os
import pwd
import socket
import logging as log
import subprocess
from time import sleep
import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem
from subprocess import check_output, call

tbb_path="/home/ubuntu/tor-browser_en-US"
geckodriver="/home/ubuntu/geckodriver/geckodriver"
socks_port=9150
test_site="https://check.torproject.org"
tbb_runnable="start-tor-browser.desktop"
# tor_runnable="/home/ubuntu/tor-browser_en-US/Browser/start-tor-browser"
# current_dir = os.path.dirname(os.path.realpath(__file__))
localhost="127.0.0.1"


def launch_tbb():
    log.info("Starting TBB...")
    pid = subprocess.Popen("./" + tbb_runnable, cwd=tbb_path).pid
    return pid

def start_strace_on_process(pid, username):
    log.info("Starting strace on %s..." % str(pid))
    subprocess.run(["strace", "-u", username, "-p", str(pid)])

def check_socket(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        if sock.connect_ex((localhost, port)) == 0:
            log.info("Port %d is open..." % port)
        else:
            log.info("Port %d is not open..." % port)


def wait_until_tbb_port_is_open():
    log.info("Checking if SOCKS port is open...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((localhost, socks_port))
    # while result != 0:
        # pass
    sock.close()

def connect_to_tbb():
    log.info("Connecting to TBB...")
    # tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_path)
    with TorBrowserDriver(tbb_path=tbb_path, tor_cfg=cm.USE_RUNNING_TOR, socks_port=socks_port, executable_path=geckodriver) as driver:
        # input("Press Enter to continue...")
        return driver

def visit_site(driver, site_name):
    log.info("Visiting site...")
    # input("Press Enter to continue...")
    driver.load(site_name)

def get_pid(proc_name):
    return check_output(["pidof"], proc_name)

def get_username():
    return pwd.getpwuid(os.getuid()).pw_name

def main():
    log.getLogger().setLevel(log.INFO)
    tbb_pid = launch_tbb()
    check_socket(socks_port)
    sleep(5)
    check_socket(socks_port)
    # wait_until_tbb_port_is_open()
    # start_strace_on_process(tbb_pid, get_username())
    driver = connect_to_tbb()
    visit_site(driver, test_site)
    # tor_process.kill()

if __name__ == '__main__':
    main()