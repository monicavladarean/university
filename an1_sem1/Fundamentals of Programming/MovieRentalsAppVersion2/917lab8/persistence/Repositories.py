class RepoError(Exception):
    pass

class RepoActor(object):
    
    
    def __init__(self):
        self.__actors = []
    
    def searchById(self,idActor):
        for actor in self.__actors:
            if actor==idActor:
                return actor
        raise RepoError("inexisting actor!")
    
    
    def store_actor(self,actor):
        if actor in self.__actors:
                raise RepoError("existing actor!")
        self.__actors.append(actor)

    def get_all(self):
        return self.__actors[:]
class RepoMovie(object):
    
    
    def __init__(self):
        self.__movies = []
    
    
    def store_movie(self,movie):
        if movie in self.__movies:
            raise RepoError("existing movie!")
        self.__movies.append(movie)

    def searchById(self,idMovie):
        for movie in self.__movies:
            if movie.get_ident()==idMovie:
                return movie
        raise RepoError("inexisting movie!")


    def get_all(self):
        return self.__movies[:]
        


class RepoCast(object):
    
    
    def __init__(self):
        self.__casts = []
    
    def store_cast(self,cast):
        if cast in self.__casts:
            raise RepoError("existing cast!")
        self.__casts.append(cast)


    def get_all(self):
        return self.__casts[:]
