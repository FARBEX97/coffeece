from SQLiteDB import SQLiteDB as db


# OBJECT INIT
path_to_db = 'test.db'
db = db(path_to_db)


# CREATE CURSOR
try:
    test_cursor = db.create_cursor()
except Exception as e:
    print(e)


# CREATE TABLE
# Expected use
cursor = test_cursor
table_name = "test_table"
table_columns = {
    "text_column": "text",
    "int_column": "int"
}
try:
    db.create_table(cursor, table_name, table_columns)
    print("CREATE TABLE 'Expected use' test passed")
except Exception as e:
    print(e)


# CREATE ROW
# Expected use
try:
    cursor = test_cursor
    table_name = "test_table"
    row_items = ["test_text_item", 1987]
    db.insert_row(cursor, table_name, row_items)
    print("CREATE ROW 'Expected use' test passed")
except Exception as e:
    print(e)




# EXPORT TABLE TO EXCEL
# Expected use
try:
    table_name = 'test_table'
    db.export_table_to_excel(table_name)
    print("EXPORT TABLE TO EXCEL 'Expected use' test passed")
except Exception as e:
    print(e)

# COMMIT CHANGES
# Expected use
try:
    db.commit_changes()
except Exception as e:
    print(e)


# CLOSE_CONNECTION
# Expected use
try:
    db.close_connection()
except Exception as e:
    print(e)
