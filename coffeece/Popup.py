import os
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showinfo, askyesno



class Popup():

    def show_info(title, message):
        """Shows a popup with the title and message provided"""
        showinfo(title,message)


    def ask_file():
        """Ask user for a file. Returns path as string"""
        path = askopenfilename()
        filename = os.path.relpath(path, '.') 
        return filename


    def ask_directory():
        """Ask user for a directory path. Returns path as string"""
        path = askdirectory()
        folder_selected = os.path.abspath(path) 
        return folder_selected


    def ask_yes_no(title, message):
        """Shows a popup with the title and message provided and ask yes-no. If yes returns 'True'"""
        return askyesno(title, message)