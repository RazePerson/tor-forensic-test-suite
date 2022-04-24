import os
import glob
import pytest
import unittest
import consts as consts

from sqlite3 import connect
from datetime import datetime
from utils.utils import Utils
from log.logger import Logging
from utils.db_utils import DBUtils
from flashtext import KeywordProcessor
from utils.system_utils import SystemUtils
from tor_browser.tor_browser_using_stem import TorBrowserUsingStem

log = Logging()
utils = Utils()

unittest.TestLoader.sortTestMethodsUsing = None


def test_util(connected_tbb):
    pass
    # connected_tbb.load_url(consts.DUCKDUCKGO_ONION)
    # log.info("Na...")
    # connected_tbb.kill_process()