from Business_Logic import *
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.rentals_repo = Rentals()
        self.clients_repo = Clients()
        self.movies_repo = Movies()
        self.business = Business(self.rentals_repo, self.clients_repo, self.movies_repo)

    def test_add_client(self):
        self.business.add_client("11","Ion")
        self.assertEqual(1,len(self.clients_repo.clients_list))

    def test_remove_client(self):
        self.business.add_client("11", "Ion")
        self.business.remove_client("11")
        self.assertEqual(0,len(self.clients_repo.clients_list))

    def test_update_client(self):
        self.business.add_client("11", "Ion")
        self.business.update_client_name("11","Gigi")
        assert self.business.clients_repo.clients_list[0].name_get()=="Gigi"

    def test_add_movie(self):
        self.business.add_movie("11","a","a","a")
        self.assertEqual(1, len(self.movies_repo.movies_list))

    def test_remove_movie(self):
        self.business.add_movie("11","a","a","a")
        self.business.remove_movie("11")
        self.assertEqual(0, len(self.movies_repo.movies_list))

    def test_update_title(self):
        self.business.add_movie("11", "a", "a", "a")
        self.business.update_movie_title("11","b")
        assert self.business.movies_repo.movies_list[0].title_get()=="b"

    def test_update_description(self):
        self.business.add_movie("11", "a", "a", "a")
        self.business.update_movie_description("11","b")
        assert self.business.movies_repo.movies_list[0].description_get()=="b"

    def test_update_genre(self):
        self.business.add_movie("11", "a", "a", "a")
        self.business.update_movie_genre("11","b")
        assert self.business.movies_repo.movies_list[0].genre_get()=="b"

    def test_rent_movie(self):
        self.business.add_client("11", "Ion")
        self.business.add_movie("11", "a", "a", "a")
        rented_date = datetime(1, 1, 1)
        due_date = datetime(2, 1, 1)
        self.business.rent_movie(rented_date, due_date, "11", "11")
        self.assertEqual(1, len(self.rentals_repo.rentals_list))

