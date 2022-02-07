from sqlite3 import connect
import pytest
import unittest
import sandbox.consts as consts

from datetime import datetime
from sandbox.utils import Utils
from sandbox.logger import Logging
from sandbox.db_utils import DBUtils
from sandbox.system_utils import SystemUtils
from sandbox.tor_browser_using_stem import TorBrowserUsingStem

log = Logging()
sys = SystemUtils()

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

def test_jetstream(jetstream_tbb):
    # connected_tbb.load_url(consts.JETSTREAM)
    # connected_tbb.start_jetstream_test()
    jetstream_tbb.kill_process()

# @pytest.mark.skip()
def test_timestamp(timestamp_closed_tbb):
    profile_dir = consts.TBB_PATH + "/" + consts.PLACEHOLDER_PROFILE_PATH_SUFFIX
    db_file = profile_dir + "/" + "storage.sqlite"

    sys = SystemUtils()
    if sys.dir_exists(consts.TEMP_TEST_DIR):
        sys.delete_dir(consts.TEMP_TEST_DIR)
        sys.create_dir(consts.TEMP_TEST_DIR)
    else:
        sys.create_dir(consts.TEMP_TEST_DIR)

    db_utils = DBUtils()
    db_utils.dump_to_csv(db_file, consts.TEMP_TEST_DIR)
    utils = Utils()
    csv_file = consts.TEMP_TEST_DIR + "/origin.csv"
    time = utils.read_csv_column(csv_file, "last_access_time")
    final_timestamp = int(str(time[0])[:-6])
    log.info("Timestamp from csv: %d - Timestamp from termination: %d " %
                (int(final_timestamp), int(timestamp_closed_tbb)))
    log.info("Timestamp date format from csv: %s - Timestamp date format from termination: %s " %
                (datetime.fromtimestamp(int(final_timestamp)), datetime.fromtimestamp(int(timestamp_closed_tbb))))
    assert (abs(final_timestamp - int(timestamp_closed_tbb)) < 5)
