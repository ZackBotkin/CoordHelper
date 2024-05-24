import sqlite3
from datetime import datetime

class QueryRunner(object):

    def __init__(self, config):
        self.config = config
        self.database_file_name = "%s\\%s.db" % (
            self.config.get("database_directory"),
            self.config.get("database_name")
        )

    def run_sql(self, sql_str):
        conn = sqlite3.connect(self.database_file_name)
        conn.execute(sql_str)
        conn.commit()

    def fetch_sql(self, sql_str):
        conn = sqlite3.connect(self.database_file_name)
        query = conn.execute(sql_str)
        results = query.fetchall()
        return results

    def create_all_tables(self):
        self.create_locations_table()
        self.create_nether_routes_table()

    def create_locations_table(self):
        sql_str = "CREATE TABLE locations(name VARCHAR, x_coord INT, y_coord INT, z_coord INT, type VARCHAR, color VARCHAR, size INT)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def create_nether_routes_table(self):
        sql_str = "CREATE TABLE nether_routes(x1 INT, z1 INT, x2 INT, z2 INT, line_width INT, line_color VARCHAR, line_dash VARCHAR)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def insert_location(self, name, x_coord, y_coord, z_coord, _type, color, size):
        sql_str = "INSERT INTO locations ('name', 'x_coord', 'y_coord', 'z_coord', 'type', 'color', 'size') VALUES ('%s', '%i', '%i', '%i', '%s', '%s', '%i')" % (name, x_coord, y_coord, z_coord, _type, color, size) 
        self.run_sql(sql_str)

    def insert_nether_route(self, x1, z1, x2, z2, line_width, line_color, line_dash):
        sql_str = "INSERT INTO nether_routes ('x1', 'z1', 'x2', 'z2', 'line_width', 'line_color', 'line_dash') VALUES ('%i', '%i', '%i', '%i', '%s', '%s', '%s')" % (x1, z1, x2, z2, line_width, line_color, line_dash)
        self.run_sql(sql_str)

    def get_all_locations(self):
        sql_str = "SELECT * FROM locations"
        return self.fetch_sql(sql_str)

    def get_all_nether_routes(self):
        sql_str = "SELECT * FROM nether_routes"
        return self.fetch_sql(sql_str)

