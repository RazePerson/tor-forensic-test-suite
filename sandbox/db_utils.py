import os
import csv
import codecs
import sqlite3
import consts as consts

from logger import Logging


class DBUtils:
    def __init__(self):
        self.log = Logging()

    def connect_db(self, db_file):
        self.log.info("Connecting to DB file: %s" % db_file)
        self.conn = sqlite3.connect(db_file)

    def get_tables(self):
        return self.execute_query(consts.SQLITE_TABLE_QUERY).fetchall()

    def execute_query(self, query):
        return self.conn.execute(query)

    def dump_to_csv(self, db_file, output_dir):
        """
        This script dumps data from a SQLite database into CSV tables
        """
        self.connect_db(db_file)
        tabs = self.get_tables()
        for tab in tabs:
            tab = tab[0]
            cols = []
            try:
                # get the column names for the current table
                cols = self.execute_query("PRAGMA table_info('%s')" % tab).fetchall()
            except:
                cols = []
            if len(cols) > 0:
                # we have columns for the table, so OK to dump it
                fname = tab + '.csv'
                print('Output: ' + fname)
                path_fname = os.path.join(output_dir, fname)
                f = codecs.open(path_fname, 'w', encoding='utf-8')
                writer = csv.writer(f, dialect=csv.excel,
                                    quoting=csv.QUOTE_ALL)
                field_name_row = []
                for col in cols:
                    col_name = col[1]
                    field_name_row.append(col_name)
                # write the field labels in first row
                writer.writerow(field_name_row)
                # now get the data
                rows = self.execute_query(consts.SQLITE_SELECT_ALL_QUERY + tab).fetchall()
                for row in rows:
                    writer.writerow(row)  # write data row
                f.closed
        print("Done! " + output_dir)
