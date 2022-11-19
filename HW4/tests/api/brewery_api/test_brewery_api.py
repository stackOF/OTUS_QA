import pytest
from random import randint
from HW4.src.base_class_api import BaseClassApi as Bc
from HW4.src.api_data import BreweryAPI as Ba
from HW4.schemas.schemas import BreweryApi


class TestBreweryApi:
    @pytest.mark.schema
    def test_single_brewery_schema(self):
        """Single Brewery (schema)"""
        response = Bc.execute_method(Ba.BASE_URL, Ba.RANDOM_BREWERY)
        assert response.status_code == 200
        BreweryApi.parse_obj(response.json()[0])

    def test_get_all_breweries_list(self):
        """All Brewery list"""
        response = Bc.execute_method(Ba.BASE_URL, "")
        assert response.status_code == 200
        assert len(response.json()) != 0

    @pytest.mark.filter
    @pytest.mark.parametrize("city", ["san diego", "knox",
                                      pytest.param("wonderland", marks=pytest.mark.xfail(reason='город-выдумка'))])
    def test_get_brewery_by_city(self, city):
        """Filter by city"""
        response = Bc.execute_method(Ba.BASE_URL, f"{Ba.FILTER_BY_CITY}={city}")
        assert response.status_code == 200
        assert response.json()[0]["city"].lower() == city

    @pytest.mark.filter
    @pytest.mark.parametrize("type_brewery", Bc.get_value(Ba.TYPE_OF_BREWERY))
    def test_get_brewery_by_sort(self, type_brewery):
        """Filter by sort of brewery"""
        response = Bc.execute_method(Ba.BASE_URL, f"{Ba.FILTER_BY_SORT_OF_BREWERY}={type_brewery}")
        assert response.status_code == 200
        assert response.json()[0]["brewery_type"].lower() == type_brewery

    @pytest.mark.parametrize("number_per_page", str(randint(1, 50)))
    def test_get_breweries_per_page(self, number_per_page):
        """Number of breweries to return"""
        response = Bc.execute_method(Ba.BASE_URL, f"{Ba.PER_PAGE}{number_per_page}")
        assert response.status_code == 200
        assert len(response.json()) == int(number_per_page)
