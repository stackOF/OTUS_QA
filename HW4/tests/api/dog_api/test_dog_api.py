import pytest
from random import randint
from HW4.src.base_class_api import BaseClassApi as Bc
from HW4.src.api_data import DogAPI as Da
from HW4.schemas.schemas import DogApi


class TestDogApi:
    def test_list_all_breeds(self):
        """List all breeds"""
        response = Bc.execute_method(Da.BASE_URL, Da.ALL_BREEDS)
        data = response.json()
        assert response.status_code == 200
        assert not len(data["message"]) == 0

    @pytest.mark.schema
    @pytest.mark.parametrize('number', str(randint(1, 50)))
    def test_multiple_random_images_schemas(self, number):
        """Single random image from all dogs collection (schema)"""
        response = Bc.execute_method(Da.BASE_URL, f'{Da.MULTIPLE_IMAGES_FORM_A_BREED}{number}')
        assert response.status_code == 200
        DogApi.parse_obj(response.json())

    @pytest.mark.boundary
    @pytest.mark.parametrize('number',
                             [1, 26, 50, pytest.param(0, marks=pytest.mark.xfail(reason="за границей допустимых")),
                              pytest.param(51, marks=pytest.mark.xfail(reason="за границей допустимых"))])
    def test_multiple_random_images_schemas(self, number):
        """Multiple random images from all dogs collection (boundary count)"""
        response = Bc.execute_method(Da.BASE_URL, f'{Da.MULTIPLE_IMAGES_FORM_A_BREED}{number}')
        assert response.status_code == 200
        assert len(DogApi.parse_obj(response.json()).message) == int(number)

    def test_check_single_random_image_status(self):
        """Single random image from all dogs collection (status in json)"""
        response = Bc.execute_method(Da.BASE_URL, Da.SINGLE_RANDOM)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"

    @pytest.mark.parametrize('breed', Da.SOME_TRUE_BREEDS_LIST)
    def test_single_random_breed_true(self, breed):
        """Random dog image from a breed (true breeds)"""
        response = Bc.execute_method(Da.BASE_URL, f'breed/{breed}/images/random')
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"

    @pytest.mark.xfail(reason="Fake breed")
    @pytest.mark.parametrize('breed_fake', Da.FAKE_BREED_LIST)
    def test_single_random_breed_fake(self, breed_fake):
        """Random dog image from a breed (fake breeds)"""
        response = Bc.execute_method(Da.BASE_URL, f'breed/{breed_fake}/images/random')
        assert response.status_code == 404
