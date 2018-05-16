from GoogleManager import Service


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
                drive.files_upload('Screenshot_1.png', 'Screenshot_1.png', 'image/png')
            elif choice == '3':
                drive.files_download('16iI1aOo3jv_H2mr8tzGt9OjDK4nJE-iZ', 'photo.jpg')
            choice = input("> ")
