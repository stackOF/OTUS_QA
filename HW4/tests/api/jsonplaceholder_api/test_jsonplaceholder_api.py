import pytest
from random import randint
from HW4.src.base_class_api import BaseClassApi as Bc
from HW4.src.api_data import JSONPLaceholderAPI as Jp
from HW4.schemas.schemas import JsonPlaceholderApiComments as Cm, JsonPlaceholderApiPosts as Ps, \
    JsonPlaceholderApiTodos as Td, JsonPlaceholderApiAlbums as Al, JsonPlaceholderApiPhotos as Ph


class TestJSONPlaceholder:
    @pytest.mark.parametrize("type_res", ["posts", "comments", "albums", "photos", "todos", "users",
                                          pytest.param("sites", marks=pytest.mark.skip(reason="ресурс удален"))])
    def test_get_all_resources_type(self, type_res):
        """Get all resources type"""
        response = Bc.execute_method(Jp.BASE_URL, type_res)
        assert response.status_code == 200
        assert len(response.json()) > 0

    @pytest.mark.post
    def test_post_method(self):
        """Test post method"""
        response = Bc.execute_method(Jp.BASE_URL, Jp.POSTS, 'post', Jp.DATA_FOR_POST)
        assert response.status_code == 201

    @pytest.mark.delete
    @pytest.mark.parametrize("number_post", str(randint(1, 100)))
    def test_delete_method(self, number_post):
        """Test delete method"""
        response = Bc.execute_method(Jp.BASE_URL, f'{Jp.DELETE_POST}{number_post}', 'delete')
        assert response.status_code == 200

    @pytest.mark.parametrize("type_res, quant", [("posts", 100), ("comments", 500), ("albums", 100),
                                                 ("photos", 5000), ("todos", 200), ("users", 10)])
    def test_get_all_resources_quant(self, type_res, quant):
        """Get and count all resources type"""
        response = Bc.execute_method(Jp.BASE_URL, type_res)
        assert response.status_code == 200
        assert len(response.json()) == quant

    @pytest.mark.schema
    @pytest.mark.parametrize("type_res", ["posts", "comments", "albums", "photos", "todos"])
    def test_get_all_resources_type(self, type_res):
        """Get and validate all (almost) resources schemas"""
        response = Bc.execute_method(Jp.BASE_URL, type_res)
        assert response.status_code == 200
        if type_res == "posts":
            Ps.parse_obj(response.json()[0])
        elif type_res == "comments":
            Cm.parse_obj(response.json()[0])
        elif type_res == "albums":
            Al.parse_obj(response.json()[0])
        elif type_res == "photos":
            Ph.parse_obj(response.json()[0])
        elif type_res == "todos":
            Td.parse_obj(response.json()[0])
