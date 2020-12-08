from Business_Logic import *
from datetime import *

class UI:
    def __init__(self,business):
        self.business=business

    def client_id_in_list_check(self,id):
        '''checks if an ID that was introduced fron the keyboard exists in the client's list. If not, it raises a ValueError'''
        id_int = int(id)
        if id_int < 0:
            raise ValueError
            return
        ok = 0
        for i in range(len(self.business.clients_repo)):
            if id == self.business.clients_repo.clients_list[i].client_id_get():
                ok = 1
        if ok == 0:
            raise ValueError

    def movie_id_in_list_check(self,id):
        '''checks if an ID that was introduced fron the keyboard exists in the movies list. If not, it raises a ValueError'''
        id_int = int(id)
        if id_int < 0:
            raise ValueError
            return
        ok = 0
        for i in range(len(self.business.movies_repo)):
            if id == self.business.movies_repo.movies_list[i].movie_id_get():
                ok = 1
        if ok == 0:
            raise ValueError

    def ui_add_client(self):
            id = input("Cliend ID: ")
            id_int = int(id)
            if id_int < 0:
                raise ValueError
                return
            for i in range(len(self.business.clients_repo)):
                if id == self.business.clients_repo.clients_list[i].client_id_get():
                    raise NameError
                    return
            name = input("Client name: ")
            self.business.clients_repo=self.business.add_client(id, name)

    def ui_remove_client(self):
            id = input("Client's ID that you want to remove: ")
            self.client_id_in_list_check(id)
            self.business.clients_repo=self.business.remove_client(id)

    def ui_update_client_name(self):
        id = input("Client's ID whose name you want to change: ")
        self.client_id_in_list_check(id)
        new_name = input("Client's new name: ")
        self.business.update_client_name(id,new_name)

    def ui_list_clients(self):
        print(self.business.clients_repo)

    def ui_add_movie(self):
        id=input("Movie ID: ")
        id_int = int(id)
        if id_int < 0:
            raise ValueError
            return
        for i in range(len(self.business.movies_repo)):
            if id == self.business.movies_repo.movies_list[i].movie_id_get():
                raise NameError
                return
        title=input("Movie title: ")
        description=input("Movie description: ")
        genre=input("Movie genre: ")
        self.business.movies_repo=self.business.add_movie(id,title,description,genre)

    def ui_remove_movie(self):
        id = input("Movie's ID that you want to remove: ")
        self.movie_id_in_list_check(id)
        self.business.remove_movie(id)

    def little_menu(self):
        print(" ")
        print("You can update: ")
        print("1. The title")
        print("2. The description")
        print("3. The genre")
        print("")

    def ui_update_movie(self):
        self.little_menu()
        command_type = input("What do you want to uppdate?")
        if command_type == "1":
            id = input("Movie's ID whose title you want to change: ")
            self.movie_id_in_list_check(id)
            new_title = input("Movie's new title: ")
            self.business.update_movie_title(id,new_title)

        elif command_type == "2":
            id = input("Movie's ID whose description you want to change: ")
            self.movie_id_in_list_check(id)
            new_description = input("Movie's new description: ")
            self.business.update_movie_description(id, new_description)

        elif command_type == "3":
            id = input("Movie's ID whose genre you want to change: ")
            self.movie_id_in_list_check(id)
            new_genre = input("Movie's new genre: ")
            self.business.update_movie_genre(id, new_genre)

        else:
            print("Invalid command!")

    def ui_list_movies(self):
        print(self.business.movies_repo)

    def ui_rent_movie(self):
        client = input("Client's ID that wants to rent: ")
        self.client_id_in_list_check(client)
        movie_id=input("Movie's ID that client wants to rent: ")
        self.movie_id_in_list_check(movie_id)
        print("Introduce the date when the client rents the movie")
        day=int(input("Day: "))
        if day<1 or day>31:
            raise SyntaxError
        month=int(input("Month: "))
        if month<1 or month>12:
            raise SyntaxError
        year=int(input("Year: "))
        rented_date=datetime(year,month,day)
        if rented_date>datetime.now():
            raise NameError

        print("Introduce the date when the client has to return the movie")
        day=int(input("Day: "))
        if day<1 or day>31:
            raise SyntaxError
        month=int(input("Month: "))
        if month<1 or month>12:
            raise SyntaxError
        year=int(input("Year: "))
        due_date=datetime(year,month,day)
        self.business.rent_movie(rented_date, due_date,client,movie_id)

    def ui_return_movie(self):
        client = input("Client's ID that wants to return: ")
        self.client_id_in_list_check(client)
        movie_id = input("Movie's ID that client wants to return: ")
        self.movie_id_in_list_check(movie_id)
        print("Introduce the date of returning")
        day=int(input("Day: "))
        if day<1 or day>31:
            raise NameError
        month=int(input("Month: "))
        if month<1 or month>12:
            raise NameError
        year=int(input("Year: "))
        returning_date=datetime(year,month,day)
        self.business.return_movie(returning_date,client,movie_id)

    def print_menu(self):
        print(" ")
        print("Opperations that you can make: ")
        print("1. Add a new client")
        print("2. Remove a certain client")
        print("3. Update a client's name")
        print("4. Show all the clients")
        print("5. Add a new movie")
        print("6. Remove a certain movie")
        print("7. Update some information for a movie")
        print("8. Show all the movies")
        print("9. Rent a movie")
        print("10. Return a movie")
        print("11. Search something")
        print("12. List all curently rented movies")
        print("13. List all late rentals, sorted in descending order of the number of days of delay")
        print("14. List the clients, in decreasing order of their renting days")
        print("15. List the movies, in decreasing order, by one chriteria")
        print("16. Undo")
        print("17. Redo")
        print(" ")

    def print_inside_menu(self):
        print(" ")
        print("You can saerch a: ")
        print("1. Movie")
        print("2. Client")


    def ui_search(self):
        self.print_inside_menu()
        command=input("What do you want to search?")
        if command=="1":
            search_element=input("Introduce the word you want to search by: ")
            self.business.search_movie(search_element)
        elif command=="2":
            search_element = input("Introduce the word you want to search by: ")
            self.business.search_client(search_element)
        else:
            print("Invalid command!")

    def ui_list_rented_movies(self):
        self.business.list_rented_movies()

    def ui_list_late_rentals(self):
        print(self.business.list_late_rentals())

    def ui_list_active_clients(self):
        print(self.business.list_active_clients())

    def menu_show(self):
        print(" ")
        print("You can list the movies in decreasing order of their:")
        print("1. Number of times they were rented")
        print("2. Number of days they were rented")

    def ui_list_movies_by(self):
        self.menu_show()
        command=input("What do you want to do?")
        if command=="1":
            print(self.business.list_movies_by_times())
        elif command=="2":
            print(self.business.list_movies_by_days())
        else:
            print("Invalid command!")

    def ui_undo(self):
        self.business.undo()

    def ui_redo(self):
        self.business.redo()

    def show(self):
        #self.business.initialize_clients()
        #self.business.initialize_movies()
        self.print_menu()
        command = input("What do you want to do? ")
        while True:
            if command == "1":
                try:
                    self.ui_add_client()
                except ValueError:
                    print("Invalid input! The ID must be a positive integer.")
                except NameError:
                    print("Invalid input! This ID is taken.")
            elif command == "2":
                try:
                    self.ui_remove_client()
                except ValueError:
                    print("Invalid input! It doesn't exist a client with this ID")
            elif command == "3":
                try:
                    self.ui_update_client_name()
                except ValueError:
                    print("Invalid input! It doesn't exist a client with this ID")
            elif command == "4":
                self.ui_list_clients()
            elif command == "5":
                try:
                    self.ui_add_movie()
                except ValueError:
                    print("Invalid input! The ID must be a positive integer.")
                except NameError:
                    print("Invalid input! This ID is taken.")
            elif command == "6":
                try:
                    self.ui_remove_movie()
                except ValueError:
                    print("Invalid input! It doesn't exist a movie with this ID")
            elif command == "7":
                try:
                    self.ui_update_movie()
                except ValueError:
                    print("Invalid input! It doesn't exist a movie with this ID")
            elif command == "8":
                self.ui_list_movies()
            elif command == "9":
                try:
                   self.ui_rent_movie()
                except ValueError:
                    print("Invalid input! This ID doesn't exist")
                except TypeError:
                   print("Invalid input! This due date has already passed")
                except SyntaxError:
                   print("Invalid input! A date has maximum 31 days and 12 months")
            elif command == "10":
                try:
                    self.ui_return_movie()
                except ValueError:
                    print("Invalid input! This ID doesn't exist")
                except NameError:
                    print("Invalid input! A date has maximum 31 days and 12 months")
                except TypeError:
                    print("Invalid input! This returning date is before the rented date")
            elif command=="11":
                self.ui_search()
            elif command == "12":
                self.ui_list_rented_movies()
            elif command == "13":
                self.ui_list_late_rentals()
            elif command == "14":
                self.ui_list_active_clients()
            elif command == "15":
                self.ui_list_movies_by()
            elif command=="16":
                try:
                    self.ui_undo()
                except ValueError:
                    print("You don't have what to undo anymore")
            elif command=="17":
                try:
                    self.ui_redo()
                except:
                    print("You don't have what to redo anymore")
            elif command=="-1":
                self.business.rentals_repo.list_rentals()
            elif command == "0":
                exit()
            else:
                print("Invalid command! Please try again!")
            #print(self.business.undo_list)
            #print(self.business.redo_list)

            self.print_menu()
            command = input("What do you want to do? ")