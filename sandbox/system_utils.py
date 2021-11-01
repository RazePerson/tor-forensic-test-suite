import os
import pwd
import socket
import subprocess
import consts as consts

from logger import Logging

class SystemUtils:

    def __init__(self):
        self.log = Logging()

    def start_strace_on_process(self, pid, username):
        self.log.info("Starting strace on %s..." % str(pid))
        subprocess.run(["strace", "-u", username, "-p", str(pid)])

    def check_if_port_is_open(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            return sock.connect_ex((consts.LOCALHOST, port)) == 0

    def get_pid(self, proc_name):
        return subprocess.check_output(["pidof", proc_name])

    def get_username(self):
        return pwd.getpwuid(os.getuid()).pw_name