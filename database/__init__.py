import sqlite3
import json


class Database():
    def __init__(self):
        self.conn = sqlite3.connect(
            'database/sqlite.db', check_same_thread=False)
        self.conn.execute('DROP TABLE IF EXISTS department')
        self.conn.execute('DROP TABLE IF EXISTS course')
        self.conn.execute('DROP TABLE IF EXISTS Building_coord_id')
        self.conn.execute('DROP TABLE IF EXISTS Building_name')
        self.conn.execute('DROP TABLE IF EXISTS Building_password')
        self.conn.execute('DROP TABLE IF EXISTS Book')
        self.conn.commit()
        self.cur = self.conn.cursor()
        sql_inits = open('database/init.sql', 'r').read()
        for sql_init in sql_inits.split(';'):
            self.conn.executescript(sql_init)
            self.conn.commit()
            self.reset_database()

    def __del__(self):
        self.conn.close()

    def reset_database(self):
        pass
        # items_data = [
        #     ('1', 'Item 1', 'Description 1', 10.99, 5),
        #     ('2', 'Item 2', 'Description 2', 19.99, 3),
        #     ('3', 'Item 3', 'Description 3', 5.99, 10)
        # ]
        #
        # self.conn.executemany(
        #     'INSERT INTO items (id, name, description, price, quantity) VALUES (?, ?, ?, ?, ?)', items_data)
        #
        # categories_data = [
        #     ('1', 'Category 1'),
        #     ('2', 'Category 2'),
        #     ('3', 'Category 3')
        # ]
        #
        # self.conn.executemany(
        #     'INSERT INTO categories (id, name) VALUES (?, ?)', categories_data)
        #
        # item_category_data = [
        #     ('1', '1'),
        #     ('1', '2'),
        #     ('2', '2'),
        #     ('3', '3')
        # ]
        #
        # self.conn.executemany(
        #     'INSERT INTO item_category (item_id, category_id) VALUES (?, ?)', item_category_data)
        # self.conn.commit()

    def run_sql(self, sql):
        try:
            cursor = self.conn.execute(sql)
            todos = cursor.fetchall()
            return todos
        except Exception as e:
            return str(e)
