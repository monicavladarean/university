class Movie:
    def __init__(self,movie_id,title,description, genre):
        '''defines a movie's atributes'''
        self.movie_id=movie_id
        self.title=title
        self.description=description
        self.genre=genre

    def  movie_id_set(self,new_movie_id):
        '''sets movie's id'''
        self.movie_id=new_movie_id

    def movie_id_get(self):
        '''return the value of movie's id'''
        return self.movie_id

    def title_set(self,new_title):
        '''sets movie's title'''
        self.title = new_title

    def title_get(self):
        '''returns the value of movie's title'''
        return self.title

    def description_set(self,new_description):
        '''sets movie's description'''
        self.description = new_description

    def description_get(self):
        '''returns the movie's description'''
        return self.description

    def genre_set(self,new_genre):
        '''sets movie's genre'''
        self.genre = new_genre

    def genre_get(self):
        '''returns the movie's title'''
        return self.genre

    def __str__(self):
        '''allows us to print a movie, by converting all it's characteristics to strings and concatenating them together'''
        return str(self.movie_id) + " " + str(self.title) + " " + str(self.description) + " " + str(self.genre)

class Client:

    def __init__(self,client_id,name):
        '''defines a client's atributes'''
        self.client_id=client_id
        self.name=name

    def  client_id_set(self,new_client_id):
        '''sets clients's id'''
        self.client_id=new_client_id

    def client_id_get(self):
        '''returns the value of a client's id'''
        return self.client_id

    def name_set(self,new_name):
        '''sets clients's name'''
        self.name = new_name

    def name_get(self):
        '''returns the a client's name'''
        return self.name

    def __str__(self):
        '''allows us to print a client, by converting all it's characteristics to strings and concatenating them together'''
        return str(self.client_id) + " " + str(self.name)

class Rental:
    def __init__(self,rental_id,movie_id,client_id,rented_date,due_date, returned_date):
        '''define's a rental's characteristics'''
        self.rental_id=rental_id
        self.movie_id=movie_id
        self.client_id=client_id
        self.rented_date=rented_date
        self.due_date=due_date
        self.returned_date=returned_date

    def rental_id_set(self,new_rental_id):
        '''sets a rental's id'''
        self.rental_id = new_rental_id

    def rental_id_get(self):
        '''returns the value of a rental's id'''
        return self.rental_id

    def movie_id_set(self,new_movie_id):
        '''sets the id of a rented movie's'''
        self.movie_id = new_movie_id

    def movie_id_get(self):
        '''returns the value of a rented movie's id'''
        return self.movie_id

    def client_id_set(self,new_client_id):
        '''sets the id for the client that rents'''
        self.client_id = new_client_id

    def client_id_get(self):
        '''returns the value of the id of a client that rented'''
        return self.client_id

    def rented_date_set(self,new_rented_date):
        '''sets the date when the movie was rented by the client'''
        self.rented_date = new_rented_date

    def rented_date_get(self):
        '''returns the date when a movie was rented'''
        return self.rented_date

    def due_date_set(self,new_due_date):
        '''sets the maximum date when the movie shoul be returned by the client'''
        self.due_date = new_due_date

    def due_date_get(self):
        '''returns the maximum date when a movie has to be returned'''
        return self.due_date

    def returned_date_set(self,new_returned_date):
        '''sets the date when the movie was returned by the client'''
        self.returned_date = new_returned_date

    def returned_date_get(self):
        '''returns the date when a movie was returned'''
        return self.returned_date

    def __str__(self):
        '''allows us to print a rental, by converting all it's characteristics to strings and concatenating them together'''
        return str(self.rental_id) + " " + str(self.movie_id)+" "+str(self.client_id)+" "+str(self.rented_date)+" "+str(self.due_date)+" "+str(self.returned_date)

