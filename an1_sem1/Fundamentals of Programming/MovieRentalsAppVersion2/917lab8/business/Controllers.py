from domain.Entities import Actor,Movie,Cast,ContractAvgDTO
class ServActor(object):
    
    
    def __init__(self, validActor, repoActor):
        self.__validActor = validActor
        self.__repoActor = repoActor
    
    def add_actor(self,ident,name,value):
        actor = Actor(ident,name,value)
        self.__validActor.validateActor(actor)
        self.__repoActor.store_actor(actor)

    def get_all_actors(self):
        return self.__repoActor.get_all()

class ServMovie(object):
    
    
    def __init__(self, validMovie, repoMovie):
        self.__validMovie = validMovie
        self.__repoMovie = repoMovie
    
    
    def add_movie(self,ident,name):
        movie = Movie(ident,name)
        self.__validMovie.validateMovie(movie)
        self.__repoMovie.store_movie(movie)

    def get_all_movies(self):
        return self.__repoMovie.get_all()
    
    
    
class ServCast(object):
    
    
    def __init__(self, validCast, repoCast, repoActor, repoMovie):
        self.__validCast = validCast
        self.__repoCast = repoCast
        self.__repoActor = repoActor
        self.__repoMovie = repoMovie
    
    def add_cast(self,role,idActor,idMovie,contract):
        actor = self.__repoActor.searchById(idActor)
        movie = self.__repoMovie.searchById(idMovie)
        cast = Cast(role,actor,movie,contract)
        self.__validCast.valideazaCast(cast)
        self.__repoCast.store_cast(cast)

    def get_contract_averages(self):
        actors = {}
        
        casts = self.__repoCast.get_all()
        for cast in casts:
            actor_id = cast.get_actor().get_ident()
            if actor_id not in actors:
                actors[actor_id]=[0,0,cast.get_actor().get_name()]
            actors[actor_id][0]+=1
            actors[actor_id][1]+=cast.get_contract()
        rez=[]
        for act in actors:
            actor = actors[act]
            rez.append(ContractAvgDTO(actor[2],actor[1]/actor[0],actor[0]))
        rez.sort(key= lambda x: x.get_avg(),reverse = True)    
        return rez

