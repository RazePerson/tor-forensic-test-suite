import os
import re
import pwd
import psutil
import signal
import shutil
import socket
import tarfile
import subprocess
import consts as consts

from log.logger import Logging

class SystemUtils:

    def __init__(self):
        self.log = Logging()

    def __start_strace_on_process(self, pid, username):
        self.log.info("Starting strace on %s..." % str(pid))
        subprocess.run(["strace", "-u", username, "-p", str(pid)])

    def strace_on_process_into_file(self, file, pids):
        self.log.info("Checking output for %s" % file)
        subprocess.Popen(["sudo", "strace", "-p", pids, "-o", file])

    def check_if_port_is_open(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            return sock.connect_ex((consts.LOCALHOST, port)) == 0

    def get_pid(self, proc_name):
        return int(subprocess.check_output(["pidof", proc_name]))

    def terminate_processes(self, pids):
        for pid in pids:
            pid = int(pid)
            if psutil.pid_exists(pid):
                self.log.info("Killing process with PID %d" % pid)
                os.kill(pid, signal.SIGTERM)

    def get_username(self):
        return pwd.getpwuid(os.getuid()).pw_name

    def strings(self, filename):
        return subprocess.getoutput("strings %s" %filename)
        # return subprocess.check_output(["strings", filename], input="text")

    def find_files(self, path, filename_regex):
        file_paths = []
        regex = re.compile(filename_regex)
        for root, dirs, files in os.walk(path):
            for file in files:
                if regex.match(file):
                    file_paths.append(os.path.join(root, file))
        return file_paths

    def grep_line_from_file(self, string, file_path):
        with open(file_path,"r") as file:
            for line in file:
                if re.search(string, line):
                    return line

    def dir_exists(self, dir_path):
        return os.path.isdir(dir_path)

    def create_dir(self, path):
        if not os.path.isdir(path):
            os.mkdir(path)

    def delete_dir(self, directory):
        if os.path.isdir(directory):
            self.log.info("Deleting directory %s" % directory)
            shutil.rmtree(directory)
        else:
            self.log.info("%s is not a directory. Not deleting." % directory)

    def create_dir_override(self, directory):
        if self.dir_exists(directory):
            self.delete_dir(directory)
            self.create_dir(directory)
        else:
            self.create_dir(directory)

    def extract_tar_file(self, file_name, destination_path):
        file = tarfile.open(file_name)

        self.log.info("Extracting %s file to %s" % (file_name, destination_path))
        file.extractall(destination_path)

    def write_to_file(self, input, file, append=False):
        mode = "w"
        if append:
            mode = "a"
        self.log.info("Writing to file %s" % file)
        file = open(file, mode)
        file.write(input)
        file.close

    def system_exit(self, message):
        self.log.fatal(message)
        raise SystemExit(1)