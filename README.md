# pycofeece
Python useful classes for office work automation.


## Popup
Tkinter popup functions to:
- show_info(title, message) -> shows a popup with the title and message provided.
- ask_file() -> popup asks for a file through file explorer. Returns path as string.
- ask_directory() -> popup asks for a directory through file explorer. Returns path as string.
- ask_yes_no(title, message) -> shows a popup with the title and message provided and ask yes-no. If yes returns 'True'.


## SysWalker
System navigation and recursion functions:
- list_files_by_type(src_directory, file_extension) -> Make a list of all the files with the given file extension in the given directory. Returns list.

## Why pycofeece
The main reason behind this little classes is that a huge part of the mechanical work at a job office can be automated through this kind of objects.
The other reason to use this is to make office scripts cleaner with an — even more — simplified dependency management.
