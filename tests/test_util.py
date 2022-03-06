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
utils = Utils()

unittest.TestLoader.sortTestMethodsUsing = None


def test_util(connected_tbb):
    pass
    # connected_tbb.load_url(consts.DUCKDUCKGO_ONION)
    # log.info("Na...")
    # connected_tbb.kill_process()