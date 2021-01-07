import sqlite3
from sqlite3 import Error

import pandas as pd

# For help:
# https://realpython.com/python-sql-libraries/#using-python-sql-libraries-to-connect-to-a-database
# https://docs.python.org/2/library/sqlite3.html

class SQLiteDB:

    def __init__(self, path_to_db):
        self.path_to_db = path_to_db
        self.connection = self.create_connection()


    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.path_to_db)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection


    def create_cursor(self):
        cursor = None
        try:
            cursor = self.connection.cursor()
            print("SQLite DB cursor created successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
        
        return cursor


    def create_table(self, cursor, table_name, table_columns):

        formatted_table_columns = ''

        # Convert table_columns dict to string with format '(item_1 type, item_2 type, ..., item_n type)' 
        for column_name, column_type in table_columns.items():
            column_name_type = column_name + ' ' + column_type
            formatted_table_columns += column_name_type + ','
        formatted_table_columns = '(' + formatted_table_columns[:-1] + ')'

        # Create table in DB
        try:
            cursor.execute(f"CREATE TABLE {table_name} {formatted_table_columns}")
            print(f"SQLite DB table '{table_name}' created successfully")

        except Error as e:
            print(f"The error '{e}' occurred")


    def insert_row(self, cursor, table_name, row_items):

        formatted_row_items = ''

        # Convert row_items list to string with format '(item_1,item_2, ..., item_n)' 
        for item in row_items:
            if isinstance(item, str):                   # Keep quotes on strings: "'string'"
                formatted_row_items += f"'{item}',"
            else:
                formatted_row_items += f"{item},"
        formatted_row_items = '(' + formatted_row_items[:-1] + ')'

        try:
            cursor.execute(f"INSERT INTO {table_name} VALUES {formatted_row_items}")
            print(f"SQLite DB row in '{table_name}' created successfully")
        except Error as e:
            print(f"The error '{e}' occurred")


    def commit_changes(self):
        self.connection.commit()

    
    def close_connection(self):
        self.connection.close()

    
    def export_table_to_excel(self, table_name):
        data = pd.read_sql_query(f"SELECT * FROM {table_name}", self.connection)
        exported = False
        while exported == False:
            try:
                data.to_excel(f"{table_name}.xlsx", index=False)
                exported = True
            except PermissionError:
                input(f"PermissionError. Close the book '{table_name}.xlsx' and press any key:")
