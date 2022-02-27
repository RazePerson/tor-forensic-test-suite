import os
import glob
import pytest
import unittest
import sandbox.consts as consts

from sqlite3 import connect
from datetime import datetime
from sandbox.utils import Utils
from sandbox.logger import Logging
from sandbox.db_utils import DBUtils
from flashtext import KeywordProcessor
from sandbox.system_utils import SystemUtils
from sandbox.tor_browser_using_stem import TorBrowserUsingStem

log = Logging()
sys = SystemUtils()
keyword_processor = KeywordProcessor()

unittest.TestLoader.sortTestMethodsUsing = None


def test_keywords(connected_tbb):
    # strings = ""
    keyword_processor.add_keyword("Mandalorian")
    # path = consts.TBB_PATH
    path = connected_tbb.tbb_path
    log.info("Checking path: " + str(path))
    for filename in glob.iglob(path + '**/**', recursive=True):
        if os.path.isfile(filename):
            strings = str(sys.strings(filename))
            keywords_found = keyword_processor.extract_keywords(strings)
            if keywords_found:
                log.info("Keyword: " + str(keywords_found) + " in file: " + str(filename))
        # sys.write_to_file(strings, "/tmp"+filename+"_strings")
    # keywords_found = keyword_processor.extract_keywords(strings)
    # log.info(keywords_found)
