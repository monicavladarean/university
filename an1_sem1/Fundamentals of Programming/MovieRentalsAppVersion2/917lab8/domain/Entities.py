class Actor(object):
    
    
    def __init__(self, ident, name, value):
        self.__ident = ident
        self.__name = name
        self.__value = value

    def __str__(self):
        return str(self.__ident)+" "+ self.__name+" "+str(self.__value)

    
    def __eq__(self, value):
        if type(value)==int:
            return self.__ident == value
        return self.__ident == value.__ident


    def get_ident(self):
        return self.__ident


    def get_name(self):
        return self.__name


    def get_value(self):
        return self.__value


    def set_name(self, value):
        self.__name = value


    def set_value(self, value):
        self.__value = value

    ident = property(get_ident, None, None, None)
    name = property(get_name, set_name, None, None)
    value = property(get_value, set_value, None, None)
    
    



class Movie(object):
    
    
    def __init__(self, ident, name):
        self.__ident = ident
        self.__name = name

    def __str__(self):
        return str(self.__ident)+" "+self.__name


    def __eq__(self, value):
        return self.__ident == value.__ident


    def get_ident(self):
        return self.__ident


    def get_name(self):
        return self.__name


    def set_name(self, value):
        self.__name = value

    ident = property(get_ident, None, None, None)
    name = property(get_name, set_name, None, None)
    
    



class Cast(object):
    
    
    def __init__(self, role, actor, movie, contract):
        self.__role = role
        self.__actor = actor
        self.__movie = movie
        self.__contract = contract

    def __str__(self):
        return self.__role+" "+str(self.__actor)+ " " + str(self.__movie)+" "+ str(self.__contract) 


    def __eq__(self, value):
        return self.__role == value.__role and self.__actor==value.__actor and self.__movie == value.__movie


    def get_role(self):
        return self.__role


    def get_actor(self):
        return self.__actor


    def get_movie(self):
        return self.__movie


    def get_contract(self):
        return self.__contract


    def set_contract(self, value):
        self.__contract = value

    role = property(get_role, None, None, None)
    actor = property(get_actor, None, None, None)
    movie = property(get_movie, None, None, None)
    contract = property(get_contract, set_contract, None, None)
    
    



class ContractAvgDTO(object):
    
    
    def __init__(self, name, avg, noMovies):
        self.__name = name
        self.__avg = avg
        self.__noMovies = noMovies

    def get_avg(self):
        return self.__avg


    def __str__(self):
        return self.__name+" has earned an average of "+str(self.__avg)+" playing in "+str(self.__noMovies)+" movies."
    avg = property(get_avg, None, None, None)

    
    



