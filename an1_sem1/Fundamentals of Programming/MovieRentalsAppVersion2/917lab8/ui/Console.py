from validation.Validators import ValidError
from persistence.Repositories import RepoError
class Console(object):
    
    
    def __ui_add_actor(self,params):
        if len(params)!=3:
            print("wrong no of params!")
            return
        ident = int(params[0])
        name = params[1]
        value = float(params[2])
        self.__servActor.add_actor(ident,name,value)
    
    
    def __ui_print_actors(self,params):
        if len(params)>0:
            print("invalid no of params!")
            return 
        actors = self.__servActor.get_all_actors()
        for actor in actors:
            print(actor)
    
    
    def __ui_add_movie(self,params):
        if len(params)!=2:
            print("wrong no of params!")
            return
        ident = int(params[0])
        name = params[1]
        self.__servMovie.add_movie(ident,name)
    
    
    def __ui_print_movies(self,params):
        if len(params)>0:
            print("invalid no of params!")
            return 
        movies = self.__servMovie.get_all_movies()
        for movie in movies:
            print(movie)
    
    
    def __ui_add_cast(self,params):
        if len(params)!=4:
            print("wrong no of params!")
            return 
        role = params[0]
        idActor = int(params[1])
        idMovie = int(params[2])
        contract = float(params[3])
        self.__servCast.add_cast(role,idActor,idMovie,contract)
    
    
    def __ui_average_contract(self,params):
        if len(params)>0:
            print("invalid no of params!")
            return
        averages = self.__servCast.get_contract_averages()
        for avg in averages:
            print(avg)
    
    
    def __init__(self, servActor, servMovie, servCast):
        self.__servActor = servActor
        self.__servMovie = servMovie
        self.__servCast = servCast
        self.__commands = {
            "addActor" : self.__ui_add_actor,
            "printActors": self.__ui_print_actors,
            "addMovie" : self.__ui_add_movie,
            "printMovies": self.__ui_print_movies,
            "addCast": self.__ui_add_cast,
            "avgContract":self.__ui_average_contract
            }
    
    def run(self):
        while True:
            cmd = input(">>")
            params = cmd.split(" ")
            if cmd == "exit":
                return
            elif params[0] in self.__commands:
                try:
                    self.__commands[params[0]](params[1:])
                except ValueError:
                    print("invalid numerical value!")
                except ValidError as ve:
                    print("Validation error!")
                    print(ve)
                except RepoError as re:
                    print("Repository error!")
                    print(re)
            else:
                print("invalid command!")
            
            
    
    
    
    



