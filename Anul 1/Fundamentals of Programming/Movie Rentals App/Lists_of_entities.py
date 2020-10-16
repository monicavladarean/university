from Entities import *
from datetime import *

class Movies:
    def __init__(self):
        '''define's a list of movies'''
        self.movies_list=[]

    def add_movie (self,movie):
        '''adds a new movie's data'''
        self.movies_list.append(movie)

    def remove_movie(self,movie_id_remove):
        '''removes a movie from the list'''
        for movie in self.movies_list:
            if movie.movie_id==movie_id_remove:
                self.movies_list.remove(movie)
                break

    def __str__(self):
        '''allows us to print the list of movies'''
        result=[str(movie) for movie in self.movies_list]
        return str(result)

    def list_movies(self):
        '''prints all the movies'''
        result = [str(movie) for movie in self.movies_list]
        print(str(result))

    def update_title(self,given_id,new_title):
        '''updates the title of one named movie'''
        for movie in self.movies_list:
            if movie.movie_id==given_id:
                movie.title_set(new_title)
                break

    def update_description(self,given_id,new_description):
        '''updates the description of one named movie'''
        for movie in self.movies_list:
            if movie.movie_id==given_id:
                movie.description_set(new_description)
                break

    def update_genre(self,given_id,new_genre):
        '''updates the genre of one named movie'''
        for movie in self.movies_list:
            if movie.movie_id==given_id:
                movie.genre_set(new_genre)
                break

    def __len__(self):
        return len(self.movies_list)

    def return_movie_title(self,id):
        for i in range(len(self.movies_list)):
            if self.movies_list[i].movie_id_get()==id:
                return self.movies_list[i].title_get()

    def return_movie_description(self,id):
        for i in range(len(self.movies_list)):
            if self.movies_list[i].movie_id_get()==id:
                return self.movies_list[i].description_get()

    def return_movie_genre(self,id):
        for i in range(len(self.movies_list)):
            if self.movies_list[i].movie_id_get()==id:
                return self.movies_list[i].genre_get()

class Clients:
    def __init__(self):
        '''define's a list of clients'''
        self.clients_list = []

    def add_client(self, client):
        '''adds a new client's data'''
        self.clients_list.append(client)

    def remove_client(self,client_id_remove):
        '''removes a client from the list'''
        for client in self.clients_list:
            if client.client_id_get()==client_id_remove:
                self.clients_list.remove(client)

    def __str__(self):
        '''allows us to print the list of clients'''
        result=[str(client) for client in self.clients_list]
        return str(result)

    def list_clients(self):
        '''prints all the clients list'''
        result = [str(client) for client in self.clients_list]
        print(str(result))

    def update_name(self,given_id,new_name):
        '''updates the name of one named client'''
        for client in self.clients_list:
            if client.client_id==given_id:
                client.name_set(new_name)
                break

    def __len__(self):
        return len(self.clients_list)

    def return_client_name(self,id):
        for i in range(len(self.clients_list)):
            if self.clients_list[i].client_id_get()==id:
                return self.clients_list[i].name_get()

class Rentals:
    def __init__(self):
        '''define's a list of rentals'''
        self.rentals_list = []

    def add_rentals(self, rental):
        '''adds a new rental's data'''
        self.rentals_list.append(rental)

    def __str__(self):
        '''allows us to print the list of rentals'''
        result=[str(rental) for rental in self.rentals_list]
        return str(result)

    def list_rentals(self):
        '''prints all rentals list'''
        result = [str(rental) for rental in self.rentals_list]
        print(str(result))

    def rent_movie(self,movie_id,client_id,rented_date,due_date):
        '''sets the date for a rented movie'''
        rental_id=len(self.rentals_list)
        rental=Rental(rental_id,movie_id,client_id,rented_date,due_date, None)
        self.add_rentals(rental)

    def return_movie(self,rental_id,return_date):
        '''sets the date for a returned movie'''
        self.rentals_list[rental_id].returned_date_set(return_date)

    def __len__(self):
        return len(self.rentals_list)

