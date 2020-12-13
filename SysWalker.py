import os
import glob

class SysWalker():

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
