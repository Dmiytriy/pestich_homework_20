import pytest
from unittest.mock import MagicMock

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService


@pytest.fixture()
def director_dao_fixture():
    director_dao = DirectorDAO(None)

    jone = Director(id=1, name='Jone')
    maxim = Director(id=2, name='Maxim')

    director_dao.get_one = MagicMock(return_value=jone)
    director_dao.get_all = MagicMock(return_value=[jone, maxim])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_fixture):
        self.director_service = DirectorService(dao=director_dao_fixture)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id == 1

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert directors is not None
        assert len(directors) > 0

    def test_create(self):
        director_d = {
            'name': 'Pol'
        }

        director = self.director_service.create(director_d)

        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            'id': 1,
            'name': 'Pol'
        }

        self.director_service.update(director_d)
