from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='movie_1', description='movie_1', trailer='movie_1', year=2020, rating=7.1)
    movie_2 = Movie(id=2, title='movie_2', description='movie_2', trailer='movie_2', year=2021, rating=7.2)
    movie_3 = Movie(id=3, title='movie_3', description='movie_3', trailer='movie_3', year=2022, rating=7.3)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    movie_dao.partially_update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "title": "Movie",
            "description": "Movie",
            "trailer": "Movie",
            "year": 2022,
            "rating": 7.5
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "Movie",
            "description": "Movie",
            "trailer": "Movie",
            "year": 2022,
            "rating": 7.5
        }

        self.movie_service.update(movie_d)

    def test_partially_update(self):
        movie_d = {
            "id": 3,
            "name": "New",
            "rating": 8.1
        }

        self.movie_service.partially_update(movie_d)