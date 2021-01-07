# Coffeece
Python useful classes for office work automation.
Currently working on Python 3.


# Install
You can install this package using pip:
```pip install coffeece```


## Popup
Tkinter popup functions to:
- show_info(title, message) -> shows a popup with the title and message provided.
- ask_file() -> popup asks for a file through file explorer. Returns path as string.
- ask_directory() -> popup asks for a directory through file explorer. Returns path as string.
- ask_yes_no(title, message) -> shows a popup with the title and message provided and ask yes-no. If yes returns 'True'.


## SQLiteDB
A class to manage SQLite3 databases. Now it could:
- create_connection(self) -> Connect with sqlite3 DB (create it if there isn't). Returns conection object.
- create_cursor(self) -> Create cursor to communicate with DB. Returns cursor.
- create_table(cursor, table_name, table_columns) -> Create a table with the name (string) columns and column types (dictionary) given by the user.
- insert_row(cursor, table_name, row_items) -> Inserts row into DB with the cursor (cursor), table name (string), and items (list) given by the user.
- commit_changes(self) -> Save DB changes.
- close_connection(self) -> Close connection to DB.
- export_table_to_excel(self, table_name) -> Exports table to excel using ```Pandas``` library.

Third party dependencies:
- Pandas


## SysWalker
System navigation and recursion functions:
- list_files_by_type(src_directory, file_extension) -> Make a list of all the files with the given file extension in the given directory. Returns list.


## Why Coffeece?
The main reason behind this little classes is that a huge part of the mechanical work at a job office can be automated through this kind of objects.
The other reason to use this is to make office scripts cleaner with an — even more — simplified dependency management.
