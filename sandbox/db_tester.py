import consts as consts

from logger import Logging
from db_utils import DBUtils

log = Logging()
db_utils = DBUtils()

def print_db_file():
    db_utils.connect_db(consts.TEST_SQLITE_FILE)
    tables = db_utils.get_tables()
    for table in tables:
        log.info("Executing select all on table: %s" % table[0])
        query = consts.SQLITE_SELECT_ALL_QUERY + table[0]
        results = db_utils.execute_query(query).fetchall()
        for result in results:
            log.info("Results: %s" % str(result))


def main():
    db_utils.dump_to_csv(consts.TEST_SQLITE_FILE, consts.CSV_DUMP_DIR)


if __name__ == '__main__':
    main()
