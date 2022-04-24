from sqlite3 import connect
import time
from importlib_metadata import csv
from numpy import size
import pytest
import unittest

from secretstorage import dbus_init
import sandbox.consts as consts

from datetime import datetime
from sandbox.utils import Utils
from sandbox.logger import Logging
from sandbox.db_utils import DBUtils
from flashtext import KeywordProcessor
from sandbox.system_utils import SystemUtils
from sandbox.tor_browser_using_stem import TorBrowserUsingStem

log = Logging()
utils = Utils()
sys = SystemUtils()
db_utils = DBUtils()

unittest.TestLoader.sortTestMethodsUsing = None


# class TestSqlite(unittest.TestCase):

# def setUp(self):
#     self.tbb = TorBrowserUsingStem(tbb_path=consts.TBB_PATH)
#     self.tbb.launch_tbb()
#     self.tbb.connect_to_tbb()
#     self.tbb.load_url(consts.JETSTREAM)
#     self.tbb.start_jetstream_test()
#     self.timestamp_before = datetime.now().timestamp()

#     log.info("Tor PID: %s" % int(sys.get_pid("tor")))

#     self.tbb.kill_process()
#     self.timestamp_after = datetime.now().timestamp()
#     timestamp_diff = int(self.timestamp_after) - int(self.timestamp_before)
#     log.info("Timestamp before: %d - Timestamp after: %d" %
#              (int(self.timestamp_before), int(self.timestamp_after)))
#     log.info("Timestamp diff: %d" % timestamp_diff)
#     self.timestamp = self.timestamp_after
#     # self.timestamp = self.timestamp_after - timestamp_diff

def _get_keywords_moz_places(tbb_path, url):
    tbb_path = tbb_path
    db_file_regex = "^places.sqlite$"
    csv_file = consts.TEMP_TEST_DIR + "/moz_places.csv"
    column = "url"
    keyword = utils.extract_url_object(url).fld
    return _find_keyword_in_db_file(
        tbb_path, db_file_regex, csv_file, column, keyword)


def _find_keyword_in_db_file(tbb_path, db_file_regex, csv_file, column, keyword):
    if len(sys.find_files(tbb_path, db_file_regex)) != 0:
        db_file = str(sys.find_files(tbb_path, db_file_regex)[0])
    else:
        return None

    sys.create_dir_override(consts.TEMP_TEST_DIR)
    db_utils.dump_to_csv(db_file, consts.TEMP_TEST_DIR)

    titles = list(utils.read_csv_column(csv_file, column).values)
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keyword(keyword)
    return keyword_processor.extract_keywords(str(titles))


@pytest.mark.skip()
def test_jetstream(jetstream_tbb):
    # connected_tbb.load_url(consts.JETSTREAM)
    # connected_tbb.start_jetstream_test()
    jetstream_tbb.kill_process()


def test_timestamp(connected_tbb):
    tbb_path = connected_tbb.tbb_profile_path
    db_file_regex = "^storage.sqlite$"
    csv_file = consts.TEMP_TEST_DIR + "/origin.csv"
    column = "last_access_time"

    time = db_utils.get_column_values(tbb_path, db_file_regex, csv_file, column)
    timestamp = connected_tbb.termination_time

    final_timestamp = int(str(time[0])[:-6])
    log.info("Timestamp from csv: %d - Timestamp from termination: %d " %
             (int(final_timestamp), int(timestamp)))
    log.info("Timestamp date format from csv: %s - Timestamp date format from termination: %s " %
             (datetime.fromtimestamp(int(final_timestamp)), datetime.fromtimestamp(int(timestamp))))
    assert (abs(final_timestamp - int(timestamp)) > 5)


# @pytest.mark.skip()
def test_keyword_in_places_sqlite(connected_tbb):
    tbb_path = connected_tbb.tbb_profile_path
    db_file_regex = "^places.sqlite$"
    csv_file = consts.TEMP_TEST_DIR + "/moz_places.csv"
    column = "title"
    keyword = "Mandalorian"
    keywords_found = _find_keyword_in_db_file(
        tbb_path, db_file_regex, csv_file, column, keyword)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True


def test_find_url_moz_places(connected_tbb):
    tbb_path = connected_tbb.tbb_profile_path
    db_file_regex = "^places.sqlite$"
    csv_file = consts.TEMP_TEST_DIR + "/moz_places.csv"
    column = "url"
    keyword = utils.extract_url_object("https://duckduckgo.com/").fld
    keywords_found = _find_keyword_in_db_file(
        tbb_path, db_file_regex, csv_file, column, keyword)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True
    # utils.download_and_extract_tor_browser("6.0.1")


@pytest.mark.skip()
def test_moz_origins_existence(connected_tbb):
    db_file = str(sys.find_files(
        connected_tbb.tbb_profile_path, "^places.sqlite$")[0])

    sys.create_dir_override(consts.TEMP_TEST_DIR)
    db_utils.dump_to_csv(db_file, consts.TEMP_TEST_DIR)
    file = sys.find_files(consts.TEMP_TEST_DIR, "^moz_origins.csv$")

    log.info("File: " + str(file))
    assert (file is None or size(file) == 0) is True


# @pytest.mark.skip()
def test_find_url_in_moz_origins(connected_tbb):
    keywords_found = _get_keywords_moz_places(
        connected_tbb.tbb_profile_path, consts.DUCKDUCKGO_URL)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True


def test_find_url_issue_22867(connected_tbb):
    keywords_found = _get_keywords_moz_places(
        connected_tbb.tbb_profile_path, consts.URL_ISSUE_22867)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True


def test_find_url_isse_24866_first_url(connected_tbb):
    keywords_found = _get_keywords_moz_places(
        connected_tbb.tbb_profile_path, consts.URL_ISSUE_24866_1)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True


def test_find_url_isse_24866_second_url(connected_tbb):
    keywords_found = _get_keywords_moz_places(
        connected_tbb.tbb_profile_path, consts.URL_ISSUE_24866_2)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True
