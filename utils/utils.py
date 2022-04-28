import re
import requests
import pandas as pd
import consts as consts

from tld import get_tld
from log.logger import Logging
from utils.system_utils import SystemUtils

sys = SystemUtils()


class Utils:

    def __init__(self):
        self.log = Logging()

    def find_url(self, string):
        regex = consts.URL_REGEX
        url = re.findall(regex, string)
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
        found_urls = ''.join(urls)
        sys.write_to_file(found_urls, tbb_path + "urls_in_bin_file")

    def download_and_extract_tor_browser(self, version):
        file_name = "tor-browser-linux64-" + version + "_en-US.tar.xz"
        url = self.__build_url(version, "")
        self.log.info("Downloading %s" % url)
        response = requests.get(url)

        tar_file = re.findall(
            ">(tor-browser-linux64-"+version+"_en-US.tar.xz)", response.text)
        if len(tar_file) == 0:
            tar_file = re.findall(
                ">(tor-browser-linux64-"+version+".*.tar.xz)", response.text)

        url = self.__build_url(version, tar_file[0])
        self.log.info(url)

        response = requests.get(url)

        directory = self.__create_download_dir(
            consts.TBB_DOWNLOAD_PATH, version)

        file_path = directory + file_name
        self.log.info("Writing response to file: %s" % file_path)
        with open(file_path, "wb") as file:
            file.write(response.content)

        sys.extract_tar_file(file_path, directory)
        return directory

    def read_csv_column(self, csv_file, column):
        df = pd.read_csv(csv_file)
        return df[column]

    def extract_url_object(self, url):
        return get_tld(url, as_object=True)

    def get_firefox_version_from_tbb_path(self, path):
        firefox_version_file = sys.find_files(
            path, consts.FIREFOX_VERSION_FILE_REGEX)

        version_line = sys.grep_line_from_file(
            consts.FIREFOX_VERSION, firefox_version_file[0])

        full_version_number = version_line.split('=')[1]

        version_number_str = full_version_number.split('.')[0]
        return int(version_number_str)

    def find_gecko_version(self, version):
        index = 0
        firefox_versions = consts.GECKO_COMPATIBILITY[consts.GC_FIREFOX]
        geckodriver_versions = consts.GECKO_COMPATIBILITY[consts.GC_GECKO]
        while index != len(firefox_versions) and version < firefox_versions[index]:
            index += 1

        if index == (len(firefox_versions)):
            return None

        return geckodriver_versions[index]

    def download_and_extract_geckodriver(self, version):
        url = consts.GECKODRIVER_RELEASE_PAGE.format(version=version)
        directory = self.__create_download_dir(
            consts.GECKODRIVER_DOWNLOAD_PATH, version)
        file_name = consts.GECKODRIVER_TAR_FILE.format(version=version)

        response = requests.get(url)

        file_path = directory + file_name
        self.log.info("Writing response to file: %s" % file_path)
        with open(file_path, "wb") as file:
            file.write(response.content)

        sys.extract_tar_file(file_path, directory)
        return directory

    def __build_url(self, version, file_name):
        tar_file_path = version + "/" + file_name
        url = consts.TOR_ARCHIVE_URLS + tar_file_path
        return url

    def __create_download_dir(self, path, version):
        directory = path + version + "/"
        self.log.info("Creating directory %s" % directory)
        sys.create_dir(path)
        sys.create_dir(directory)
        return directory

    def __exclude_from_list(self, source_list, exclusion_list):
        return [i for i in source_list if i not in exclusion_list]
