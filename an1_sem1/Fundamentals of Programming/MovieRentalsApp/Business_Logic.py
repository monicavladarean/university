from Lists_of_entities import *
from Undo import *
import string
import random
from sorting import *

class Business():
    def __init__(self,rentals_repo,clients_repo,movies_repo):
        '''defines the 3 lists of objects that we work with: rentals, clients and movies'''
        self.rentals_repo = rentals_repo
        self.clients_repo = clients_repo
        self.movies_repo = movies_repo
        self.undo_list=[]
        self.redo_list =[]

    def initialize_clients(self):
        self.clients_repo.add_client(Client("1", "Ion Popescu"))
        self.clients_repo.add_client(Client("2", "Gigel Pop"))
        self.clients_repo.add_client(Client("3", "Ionel Ciucure"))
        self.clients_repo.add_client(Client("4", "Vasile Grecu"))
        self.clients_repo.add_client(Client("5", "Mariana Papuc"))
        self.clients_repo.add_client(Client("6", "Iulia Vintila"))
        self.clients_repo.add_client(Client("7", "Carmen Suciu"))
        self.clients_repo.add_client(Client("8", "Septimiu Popica"))
        self.clients_repo.add_client(Client("9", "Amalia Gog"))
        self.clients_repo.add_client(Client("10", "Maria Velt"))

    def initialize_movies(self):
        self.movies_repo.add_movie(Movie("1", "Spiderman","most voted","cartoon"))
        self.movies_repo.add_movie(Movie("2", "Mister Bean","good for kids","commedy"))
        self.movies_repo.add_movie(Movie("3", "Dead men","scary","horror"))
        self.movies_repo.add_movie(Movie("4", "LalaLand","12+","drama"))
        self.movies_repo.add_movie(Movie("5", "Toy Story","kid friendly","cartoon"))
        self.movies_repo.add_movie(Movie("6", "Tom and Jerry","nice","cartoon"))
        self.movies_repo.add_movie(Movie("7", "Blended","laugh much here","commedy"))
        self.movies_repo.add_movie(Movie("8", "Pokemon","old but gold","anime"))
        self.movies_repo.add_movie(Movie("9", "Bakugan","most loved by kids","anime"))
        self.movies_repo.add_movie(Movie("10", "Amelie","18+","horror"))


    def add_client(self,id,name):
        '''adds a new client to the list of clients'''
        new_client = Client(id,name)
        self.clients_repo.add_client(new_client)

        self.undo_list.append(["remove_client",new_client.client_id_get()])

        client_id=new_client.client_id_get()
        self.redo_list.append(["add_client",client_id ,new_client.name_get()])

        return self.clients_repo

    def remove_client (self,id):
        '''removes a named client from the clients list'''
        client_name = self.clients_repo.return_client_name(id)

        self.clients_repo.remove_client(id)

        self.undo_list.append(["add_client", id,client_name])

        self.redo_list.append(["remove_client", id])

        return self.clients_repo

    def update_client_name(self,id,new_name):
        '''updates the name of a named client'''
        client_name = self.clients_repo.return_client_name(id)

        self.clients_repo.update_name(id, new_name)

        self.undo_list.append(["update_client", id, client_name])

        self.redo_list.append(["update_client", id, new_name])

    def add_movie(self,id,title,description,genre):
        '''adds a new movie to the list of movies'''
        new_movie=Movie(id,title,description,genre)
        self.movies_repo.add_movie(new_movie)

        self.undo_list.append(["remove_movie", new_movie.movie_id_get()])

        self.redo_list.append(["add_movie", new_movie.movie_id_get(),new_movie.title_get(),new_movie.description_get(),new_movie.genre_get()])

        return self.movies_repo

    def remove_movie(self,id):
        '''removes a named movie from the movies list'''
        movie_title = self.movies_repo.return_movie_title(id)
        movie_description = self.movies_repo.return_movie_description(id)
        movie_genre = self.movies_repo.return_movie_genre(id)

        self.movies_repo.remove_movie(id)

        self.undo_list.append(["add_movie", id,movie_title,movie_description,movie_genre])

        self.redo_list.append(["remove_movie", id])

    def update_movie_title(self,id,new_title):
        '''update's the title of a named movie'''
        movie_title = self.movies_repo.return_movie_title(id)

        self.movies_repo.update_title(id, new_title)

        self.undo_list.append(["update_movie_title", id, movie_title])

        self.redo_list.append(["update_movie_title", id, new_title])

    def update_movie_description(self,id,new_description):
        '''update's the description of a named movie'''
        movie_description = self.movies_repo.return_movie_description(id)

        self.movies_repo.update_description(id, new_description)

        self.undo_list.append(["update_movie_description", id, movie_description])

        self.redo_list.append(["update_movie_description", id, new_description])

    def update_movie_genre(self,id,new_genre):
        '''update's the genre of a named movie'''
        movie_genre = self.movies_repo.return_movie_genre(id)

        self.movies_repo.update_genre(id, new_genre)

        self.undo_list.append(["update_movie_genre", id, movie_genre])

        self.redo_list.append(["update_movie_genre", id, new_genre])

    def rent_movie(self,rented_date, due_date,client,movie_id):
        '''sets the information when a moovie is rented. it sets the date when it was rented and the date when it should be returned'''
        ok=1
        for rental in self.rentals_repo.rentals_list:
            if rental.movie_id==movie_id and rental.returned_date==None:
                ok=0
                break
        if ok==1:
            verify=1
            for rental in self.rentals_repo.rentals_list:
                if rental.client_id == client and rental.returned_date!= None and rental.due_date<rental.returned_date:
                    verify = 0
                    break
            if verify==1:
                self.rentals_repo.rent_movie(movie_id,client,rented_date,due_date)

    def return_movie(self,returning_date,client,movie_id):
        '''sets the rental's returned date when a movie is returned'''
        for rental in reversed(self.rentals_repo.rentals_list):
            if rental.client_id==client and rental.movie_id==movie_id and rental.returned_date==None:
                if returning_date<rental.rented_date_get():
                    raise TypeError
                    return
                rental.returned_date_set(returning_date)

    def search_movie(self,search_element):
        '''searches a movie by a word that is in its charachteristics'''
        search_element=search_element.lower()
        for i in range(len(self.movies_repo)):
            if self.movies_repo.movies_list[i].title_get().lower().find(search_element)!=-1 or self.movies_repo.movies_list[i].movie_id_get().find(search_element)!=-1 or self.movies_repo.movies_list[i].genre_get().lower().find(search_element)!=-1 or self.movies_repo.movies_list[i].description_get().lower().find(search_element)!=-1:
                print(self.movies_repo.movies_list[i])

    def search_client(self,search_element):
        '''searches a client by a word that is in its charachteristics'''
        search_element=search_element.lower()
        for i in range(len(self.clients_repo)):
            if self.clients_repo.clients_list[i].name_get().lower().find(search_element)!=-1 or self.clients_repo.clients_list[i].client_id_get().find(search_element)!=-1:
                print(self.clients_repo.clients_list[i])

    def list_rented_movies(self):
        '''lists, on the screen, all the rented movies at the moment'''
        for i in range(len(self.rentals_repo)):
            if self.rentals_repo.rentals_list[i].returned_date_get()==None:
                for j in range(len(self.movies_repo)):
                    if self.rentals_repo.rentals_list[i].movie_id_get()==self.movies_repo.movies_list[j].movie_id_get():
                        print(self.movies_repo.movies_list[j])

#AICI

    def list_late_rentals(self):
        '''lists, on the screen, all the rented movies that passed the returning date, sorted in decreasing order of the number of days that passed from the due date'''
        rented_rentals=Rentals()
        for i in range(len(self.rentals_repo)):
            if self.rentals_repo.rentals_list[i].returned_date_get()==None and self.rentals_repo.rentals_list[i].due_date_get()<datetime.today():
                rented_rentals.add_rentals(self.rentals_repo.rentals_list[i])
        for i in range(len(rented_rentals)-1):
            for j in range(i+1,len(rented_rentals)):

                days_1= (datetime.today() - rented_rentals.rentals_list[i].due_date_get()).days
                days_2=(datetime.today() - rented_rentals.rentals_list[j].due_date_get()).days

                if  days_1<days_2:
                    aux=rented_rentals.rentals_list[i]
                    rented_rentals.rentals_list[i]=rented_rentals.rentals_list[j]
                    rented_rentals.rentals_list[j]=aux
        return rented_rentals

    def list_active_clients(self):
        '''list most active clients, in descending order of the number of days of renting'''
        active_clients=dict()
        for i in range(len(self.clients_repo)):
            active_clients[self.clients_repo.clients_list[i].client_id_get()]=0

        for i in range(len(self.rentals_repo)):
            active_clients[self.rentals_repo.rentals_list[i].client_id_get()]+=1
        active_clients=sorted(active_clients.items(),key=lambda t: t[1], reverse=True)
        clients=Clients()
        for client in active_clients:
            client_id=client[0]
            for i in range(len(self.clients_repo)):
                if self.clients_repo.clients_list[i].client_id_get()==client_id:
                    clients.add_client(self.clients_repo.clients_list[i])

        return clients

    def list_movies_by_times(self):
        '''lists the movies, in decreasing order of the number of times that they were rented'''
        loved_movies=dict()
        for i in range(len(self.movies_repo)):
            loved_movies[self.movies_repo.movies_list[i].movie_id_get()]=0

        for i in range(len(self.rentals_repo)):
            loved_movies[self.rentals_repo.rentals_list[i].movie_id_get()]+=1
        loved_movies = sorted(loved_movies.items(), key=lambda t: t[1], reverse=True)
        movies = Movies()
        for movie in loved_movies:
            movie_id = movie[0]
            for i in range(len(self.movies_repo)):
                if self.movies_repo.movies_list[i].movie_id_get() == movie_id:
                    movies.add_movie(self.movies_repo.movies_list[i])
        return movies

    def list_movies_by_days(self):
        '''lists the movies, in decreasing order of the number of days that they were rented'''
        loved_movies = dict()
        for i in range(len(self.movies_repo)):
            loved_movies[self.movies_repo.movies_list[i].movie_id_get()] = 0

        for i in range(len(self.rentals_repo)):
            if self.rentals_repo.rentals_list[i].returned_date_get()!=None:
                days=(self.rentals_repo.rentals_list[i].returned_date_get()-self.rentals_repo.rentals_list[i].rented_date_get()).days
            else:
                days = (datetime.now() - self.rentals_repo.rentals_list[i].rented_date_get()).days

            loved_movies[self.rentals_repo.rentals_list[i].movie_id_get()] += days
        loved_movies = sorted(loved_movies.items(), key=lambda t: t[1], reverse=True)
        movies = Movies()
        for movie in loved_movies:
            movie_id = movie[0]
            for i in range(len(self.movies_repo)):
                if self.movies_repo.movies_list[i].movie_id_get() == movie_id:
                    movies.add_movie(self.movies_repo.movies_list[i])
        return movies

#AICI

    def undo(self):
        '''undo's the last operation. So, add=>remove, remove=>add, update=>update'''
        if len(self.undo_list)==0:

            raise ValueError
            return
        undo_element=self.undo_list.pop()
        operation=undo_element[0]
        id=undo_element[1]
        if len(undo_element)==2:
            if operation=="remove_client":

                self.clients_repo.remove_client(id)

            elif operation == "remove_movie":
                self.movies_repo.remove_movie(id)
        elif len(undo_element)==3:
            if operation=="add_client":
                name=undo_element[2]
                client=Client(id,name)
                self.clients_repo.add_client(client)
            elif operation=="update_client":
                name = undo_element[2]
                self.clients_repo.update_name(id,name)

            elif operation == "update_movie_title":
                movie_title=undo_element[2]
                self.movies_repo.update_title(id,movie_title)
            elif operation == "update_movie_genre":
                movie_genre = undo_element[2]
                self.movies_repo.update_genre(id, movie_genre)
            elif operation == "update_movie_description":
                movie_description= undo_element[2]
                self.movies_repo.update_description(id, movie_description)

        elif len(undo_element)==5:
            if operation=="add_movie":
                movie_title = undo_element[2]
                movie_description = undo_element[3]
                movie_genre = undo_element[4]
                movie=Movie(id,movie_title,movie_description,movie_genre)
                self.movies_repo.add_movie(movie)


    def redo(self):
        '''redo's the operation that was undo'ed'''

        redo_element = self.redo_list.pop(0)
        operation = redo_element[0]
        id = redo_element[1]
        if len(redo_element) == 2:
            if operation == "remove_client":

                self.clients_repo.remove_client(id)

            elif operation == "remove_movie":
                self.movies_repo.remove_movie(id)
        elif len(redo_element) == 3:
            if operation == "add_client":
                name = redo_element[2]
                client = Client(id, name)
                self.clients_repo.add_client(client)
            elif operation == "update_client":
                name = redo_element[2]
                self.clients_repo.update_name(id, name)

            elif operation == "update_movie_title":
                movie_title = redo_element[2]
                self.movies_repo.update_title(id, movie_title)
            elif operation == "update_movie_genre":
                movie_genre = redo_element[2]
                self.movies_repo.update_genre(id, movie_genre)
            elif operation == "update_movie_description":
                movie_description = redo_element[2]
                self.movies_repo.update_description(id, movie_description)

        elif len(redo_element) == 5:
            if operation == "add_movie":
                movie_title = redo_element[2]
                movie_description = redo_element[3]
                movie_genre = redo_element[4]
                movie = Movie(id, movie_title, movie_description, movie_genre)
                self.movies_repo.add_movie(movie)


