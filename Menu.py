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
              "4. Search for a File\n"
              "If you want to finish working just write EXIT")

    @staticmethod
    def userchoice(drive, service):
        itemlist = []
        choice = input("> ")
        while choice != 'exit':
            if choice == '1':
                print("Write the amount of last added files you want to see: ")
                amountoffiles = input("> ")
                itemlist = drive.files_list(amountoffiles, service)
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
                print("From the last chosen by you list choose the file number you want to download")
                file_number = int(input("> "))
                chosenid = itemlist[file_number]['id']
                chosenname = itemlist[file_number]['name']
                drive.files_download(chosenid, chosenname)
            elif choice == '4':
                print("choose by what phrase do you want to find the file")
                phrase = input("> ")
                itemlist = drive.files_search(100, phrase)
            choice = input("> ")
