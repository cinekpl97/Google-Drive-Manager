from GoogleManager import Service
from Menu import Menu


def main():
    drive_functions = Service()
    service = drive_functions.authorization()
    menu = Menu()
    menu.printoptions()
    menu.userchoice(drive_functions, service)


if __name__ == '__main__':
    main()
