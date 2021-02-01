import os
import glob

from zipfile import ZipFile 




def list_all_files(src_directory):
    """Make a list of all the files in the given directory. Returns list."""
    cwd = os.getcwd()
    os.chdir(src_directory)
    files = []

    for file in glob.glob("*"):
        files.append(file)
    os.chdir(cwd)

    return files


def list_all_files_recursively(src_directory):
    """
    Make a dictionary of all the files in the given directory recursively.
    Returns dictionary = root: { dirs: {} , files: {} }
    """
    cwd = os.getcwd()
    os.chdir(src_directory)
    files_tree = {}

    for root, dirs, files in os.walk(src_directory, topdown=True):
        files_tree[root] = {}
        files_tree[root]["dirs"] = dirs
        files_tree[root]["files"] = files
    
    os.chdir(cwd)

    return files_tree


def list_files_by_type(src_directory, file_extension):
    """Make a list of all the files with the given file extension in the given directory. Returns list."""
    cwd = os.getcwd()
    os.chdir(src_directory)
    files = []

    for file in glob.glob("*" + file_extension):
        file = file.replace(file_extension,"")
        files.append(file)
    os.chdir(cwd)

    return files


def open_zip_file(filepath):
    """Opens zip file and extracts all its content"""
    with ZipFile(filepath, 'r') as zip: 
        zip.extractall() 