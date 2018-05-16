import GoogleManager


class Menu:
    def __init__(self):
        print("Welcom!")

    @staticmethod
    def printoptions():
        print("What do you want to do my darling?\n"
              "1. Show me the list of last added files\n"
              "2. Upload file\n"
              "3. Download file\n")

    @staticmethod
    def userchoice():
        choice = input("Your Choice: ")
        return choice
