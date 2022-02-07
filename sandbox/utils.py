import csv
import re
import requests
import pandas as pd
import sandbox.consts as consts

from sandbox.logger import Logging
from sandbox.system_utils import SystemUtils

sys = SystemUtils()

class Utils:

    def __init__(self):
        self.log = Logging()

    def find_url(self, string):
        regex = consts.URL_REGEX
        url = re.findall(regex,string)      
        return [x[0] for x in url]

    def find_urls_in_file(self, file, excluded_urls=None):
        file_strings = sys.strings(file)
        urls = self.find_url(file_strings)
        if excluded_urls is None:
            return '\n'.join(urls)
        else:
            return '\n'.join(self.__exclude_from_list(urls, consts.EXCLUDED_URLS))

    def print_urls_from_files(self, tbb_path, file_regex):
        file_paths = sys.find_files(tbb_path, file_regex)
        file_strings = ""
        for file in file_paths:
            file_strings = sys.strings(file)
        
        urls = self.find_url(file_strings)
        excluded_urls = ""
        # print("Found urls:")
        # found_urls = ''.join(utils.exclude_from_list(urls, consts.EXCLUDED_URLS))
        found_urls = ''.join(urls)
        sys.write_to_file(found_urls, tbb_path + "urls_in_bin_file")

    def download_and_extract_tor_browser(self, version):
        file_name = "tor-browser-linux64-" + version + "_en-US.tar.xz"
        url = self.__build_url(version, file_name)
        self.log.info("Downloading %s" % url)
        response = requests.get(url)

        directory = self.__create_download_dir(version)

        file_path = directory + file_name
        self.log.info("Writing response to file: %s" % file_path)
        with open(file_path, "wb") as file:
            file.write(response.content)

        sys.extract_tar_file(file_path, directory)
        return directory

    def read_csv_column(self, csv_file, column):
        df = pd.read_csv(csv_file)
        return df[column]

    def __build_url(self, version, file_name):
        tar_file_path = version + "/" + file_name
        url = consts.TOR_ARCHIVE_URLS + tar_file_path
        return url

    def __create_download_dir(self, version):
        directory = consts.TBB_DOWNLOAD_PATH + version + "/"
        self.log.info("Creating directory %s" % directory)
        sys.create_dir(consts.TBB_DOWNLOAD_PATH)
        sys.create_dir(directory)
        return directory

    def __exclude_from_list(self, source_list, exclusion_list):
        return [i for i in source_list if i not in exclusion_list]