from Lists_of_entities import *
import pickle

class Clients_Pickle_File(Clients):
    def __init__(self,fileName='clients.pickle'):
        Clients.__init__(self)
        self.fileName=fileName
        self.loadFile()

    def loadFile(self):
        file = open(self.fileName, "rb")
        while True:
            try:
                client=pickle.load(file)
                Clients.add_client(self,client)
            except EOFError:
                break

    def saveFile(self):
            file=open(self.fileName,"wb")
            for client in self.clients_list:
                pickle.dump(client,file)

    def add_client(self, client):
        Clients.add_client(self, client)
        self.saveFile()

    def remove_client(self,client_id_remove):
        Clients.remove_client(self,client_id_remove)
        self.saveFile()

    def update_name(self,given_id,new_name):
        Clients.update_name(self,given_id,new_name)
        self.saveFile()


class Movies_Pickle_File(Movies):
    def __init__(self, fileName='movies.pickle'):
        Movies.__init__(self)
        self.fileName = fileName
        self.loadFile()

    def loadFile(self):
        file = open(self.fileName, "rb")
        while True:
            try:
                movie = pickle.load(file)
                Movies.add_movie(self, movie)
            except EOFError:
                break

    def saveFile(self):
        file = open(self.fileName, "wb")
        for movie in self.movies_list:
            pickle.dump(movie, file)

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


class Rentals_Pickle_File(Rentals):
    def __init__(self, fileName='rentals.pickle'):
        Rentals.__init__(self)
        self.fileName = fileName
        self.loadFile()

    def loadFile(self):
        file = open(self.fileName, "rb")
        while True:
            try:
                rental = pickle.load(file)
                Rentals.add_rentals(self, rental)
            except EOFError:
                break

    def saveFile(self):
        file = open(self.fileName, "wb")
        for object in self.rentals_list:
            pickle.dump(object, file)

    def add_rentals(self, rental):
        Rentals.add_rentals(self, rental)
        self.saveFile()

    def rent_movie(self,movie_id,client_id,rented_date,due_date):
        Rentals.rent_movie(self,movie_id,client_id,rented_date,due_date)
        self.saveFile()

    def return_movie(self,rental_id,return_date):
        Rentals.return_movie(self,rental_id,return_date)
        self.saveFile()
