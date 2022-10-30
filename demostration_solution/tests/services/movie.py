import pytest
from unittest.mock import MagicMock

from demostration_solution.dao.movie import MovieDAO
from demostration_solution.dao.model.movie import Movie
from demostration_solution.service.movie import MovieService


@pytest.fixture()
def movie_dao_fixture():
    movie_dao = MovieDAO(None)

    movie1 = Movie(
        id=1,
        title="Йеллоустоун",
        description="Владелец ранчо пытается",
        trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
        year=2018,
        rating=8.6,
        genre_id=1,
        director_id=1
    )
    movie2 = Movie(
        id=2,
        title="Омерзительная восьмерка",
        description="Владелец ранчо пытается",
        trailer="https://www.youtube.com/watch?v=lmB9VWm0okU",
        year=2015,
        rating=7.8,
        genre_id=2,
        director_id=2
    )

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_fixture):
        self.movie_service = MovieService(dao=movie_dao_fixture)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 1

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "description": "События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...",
            "rating": 6.0,
            "id": 3,
            "title": "Вооружен и очень опасен",
            "year": 1978,
            "trailer": "https://www.youtube.com/watch?v=hLA5631F-jo"

        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "rating": 200
        }

        self.movie_service.update(movie_d)
