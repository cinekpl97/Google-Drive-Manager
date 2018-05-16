from GoogleManager import Service
from Menu import Menu

menu = Menu()
menu.printoptions()
drive = Service()
service = drive.authorization()
drive.files_list(10, service)
