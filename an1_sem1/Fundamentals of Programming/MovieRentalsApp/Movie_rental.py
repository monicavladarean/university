from Text_File_Repo import *
from Pickle_File_Repo import *
from UI import *

f=open("settings.properties.txt","r")
set=f.read()
set=set.split("=")

if set[1]=="inmemory":
    rentals_repo = Rentals()
    clients_repo = Clients()
    movies_repo = Movies()

elif set[1]=="binaryfiles":
    rentals_repo=Rentals_Pickle_File()
    clients_repo=Clients_Pickle_File()
    movies_repo=Movies_Pickle_File()

elif set[1]=="textfiles":
    rentals_repo = Rentals_Text_File()
    clients_repo = Clients_Text_File()
    movies_repo = Movies_Text_File()
else:
    exit()

business=Business(rentals_repo,clients_repo,movies_repo)

ui=UI(business)
ui.show()



