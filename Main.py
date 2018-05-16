from GoogleManager import Service
from Menu import Menu
import os


def main():
    drive = Service()
    service = drive.authorization()
    menu = Menu()
    menu.printoptions()
    menu.userchoice(drive, service)


if __name__ == '__main__':
    main()
