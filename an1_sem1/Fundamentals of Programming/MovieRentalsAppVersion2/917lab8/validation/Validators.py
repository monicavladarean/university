class ValidError(Exception):
    pass

class ValidActor(object):
    
    
    def __init__(self):
        pass
    
    def validateActor(self,actor):
        errors = ""
        if actor.get_ident()<0:
            errors += 'invalid ident!\n'
        if len(errors)>0:
            raise ValidError(errors)
    



class ValidMovie(object):
    
    
    def __init__(self):
        pass
    
    def validateMovie(self,movie):
        errors = ""
        if movie.get_ident()<0:
            errors += 'invalid ident!\n'
        if len(errors)>0:
            raise ValidError(errors)
    



class ValidCast(object):
    
    
    def __init__(self):
        pass
    
    
    def valideazaCast(self,cast):
        errors = ""
        if cast.get_contract()<1000:
            errors += 'invalid contract!\n'
        if len(errors)>0:
            raise ValidError(errors)


