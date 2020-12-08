from Lists_of_entities import *

class Clients_Text_File(Clients):
    def __init__(self,fileName='clients.txt'):
        Clients.__init__(self)
        self.fileName=fileName
        self.loadFile()

    def loadFile(self):
        try:
            file=open(self.fileName,"r")
            line=file.readline()
            while len(line)>2:
                tok=line.split(",")
                client=Client(tok[0],tok[1])
                Clients.add_client(self,client)
                line=file.readline()
            file.close()
        except IOError:
            raise ValueError("Error!")

    def saveFile(self):
        try:
            file=open(self.fileName,"w")
            for client in self.clients_list:
                file.write(str(client.client_id_get())+" , "+str(client.name_get()) + '\n')
            file.close()
        except IOError:
            raise ValueError("Error!")


    def add_client(self, client):
        Clients.add_client(self, client)
        self.saveFile()

    def remove_client(self,client_id_remove):
        Clients.remove_client(self,client_id_remove)
        self.saveFile()

    def update_name(self,given_id,new_name):
        Clients.update_name(self,given_id,new_name)
        self.saveFile()


class Movies_Text_File(Movies):
    def __init__(self, fileName='movies.txt'):
        Movies.__init__(self)
        self.fileName = fileName
        self.loadFile()

    def loadFile(self):
        try:
            file = open(self.fileName, "r")
            line = file.readline()
            while len(line) > 2:
                tok = line.split(",")
                movie = Movie(tok[0], tok[1], tok[2], tok[3])
                Movies.add_movie(self, movie)
                line = file.readline()
            file.close()
        except IOError:
            raise ValueError("Error!")

    def saveFile(self):
        try:
            file = open(self.fileName, "w")
            for movie in self.movies_list:
                file.write(str(movie.movie_id_get()) + " , " + str(movie.title_get()) + " , " + str(movie.description_get()) + " , "+ str(
                    movie.genre_get())+ '\n')
            file.close()
        except IOError:
            raise ValueError("Error!")

    def add_movie(self, movie):
        Movies.add_movie(self, movie)
        self.saveFile()

    def remove_movie(self, movie_id_remove):
        Movies.remove_movie(self, movie_id_remove)
        self.saveFile()

    def update_description(self, given_id, new_description):
        Movies.update_description(self, given_id, new_description)
        self.saveFile()

    def update_genre(self, given_id, new_genre):
        Movies.update_genre(self, given_id, new_genre)
        self.saveFile()

    def update_title(self, given_id, new_title):
        Movies.update_title(self, given_id, new_title)
        self.saveFile()


class Rentals_Text_File(Rentals):
    def __init__(self, fileName='rentals.txt'):
        Rentals.__init__(self)
        self.fileName = fileName
        self.loadFile()

    def loadFile(self):
        try:
            file = open(self.fileName, "r")
            line = file.readline()
            while len(line) > 2:
                tok = line.split(",")
                rental = Rental(tok[0], tok[1], tok[2], tok[3], tok[4], tok[5],tok[6])
                Rentals.add_rentals(self, rental)
                line = file.readline()
            file.close()
        except IOError:
            raise ValueError("Error!")

    def saveFile(self):
        try:
            file = open(self.fileName, "w")
            for rental in self.rentals_list:
                file.write(str(rental.rental_id_get()) + "," + str(rental.movie_id_get())+","+str(rental.client_id_get())+" , "+str(rental.rented_date_get())+","+str(rental.due_date_get())+" , "+str(rental.returned_date_get())+ '\n' )
            file.close()
        except IOError:
            raise ValueError("Error!")

    def add_rentals(self, rental):
        Rentals.add_rentals(self, rental)
        self.saveFile()

    def rent_movie(self,movie_id,client_id,rented_date,due_date):
        Rentals.rent_movie(self,movie_id,client_id,rented_date,due_date)
        self.saveFile()

    def return_movie(self,rental_id,return_date):
        Rentals.return_movie(self,rental_id,return_date)
        self.saveFile()
