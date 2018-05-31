from GoogleManager import Service
from tkinter import *
from tkinter import filedialog
import ntpath
import mimetypes


class Menu:
    def __init__(self):
        print("Welcome!")

    @staticmethod
    def printoptions():
        print("What do you want to do my darling?\n"
              "1. Show me the list of last added files\n"
              "2. Upload file\n"
              "3. Download file\n"
              "If you want to finish working just write EXIT")

    @staticmethod
    def userchoice(drive, service):
        choice = input("> ")
        while choice != 'EXIT':
            if choice == '1':
                print("Write the amount of last added files you want to see: ")
                amountoffiles = input("> ")
                drive.files_list(amountoffiles, service)
            elif choice == '2':
                window = Tk()
                window.filename = filedialog.askopenfilename(initialdir='/', title="Select document",
                                                             filetypes=(("All Files", "*.*"), ("Text Files", "*.txt")))
                path = window.filename
                filename = ntpath.basename(path)
                mime = mimetypes.guess_type(path)
                mimetype = mime[0]
                drive.files_upload(filename, path, mimetype)
            elif choice == '3':
                drive.files_download('16iI1aOo3jv_H2mr8tzGt9OjDK4nJE-iZ', 'photo.jpg')
            choice = input("> ")
