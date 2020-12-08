from validation.Validators import ValidActor,ValidMovie,ValidCast
from persistence.Repositories import RepoActor,RepoMovie,RepoCast
from business.Controllers import ServActor,ServMovie,ServCast
from ui.Console import Console

repoMovie = RepoMovie()
validMovie = ValidMovie()
servMovie = ServMovie(validMovie,repoMovie)

servMovie.add_movie(1, "Morometii2")
servMovie.add_movie(2, "Ronin")



repoActor = RepoActor()
validActor = ValidActor()
servActor=ServActor(validActor,repoActor)

servActor.add_actor(1, "TomCruise", 23.45)
servActor.add_actor(2, "JackBlack", 223.45)



repoCast = RepoCast()
validCast = ValidCast()
servCast = ServCast(validCast,repoCast,repoActor,repoMovie)

servCast.add_cast("ilie", 1, 1, 42332132)
servCast.add_cast("cochilie", 1, 2, 423122332)
servCast.add_cast("iliutza", 1, 2, 31342332)
servCast.add_cast("ile", 2, 1, 4332)
servCast.add_cast("ilie", 2, 2, 4122)


c= Console(servActor,servMovie,servCast)
c.run()