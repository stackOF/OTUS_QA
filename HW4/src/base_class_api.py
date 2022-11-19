import requests


class BaseClassApi:

    @staticmethod
    def execute_method(base_url, endpoint=None, method='get', json_data=None):
        """ Определение типа метода и его выполнение"
        :param base_url: базовый URL
        :param endpoint: endpoint
        :param method: метод: 'get' или 'post'. По умолчанию - 'get'
        :param json_data: данные json, используется для POST запросов"""
        response = None
        if method == 'get':
            try:
                response = requests.get(url=f'{base_url}{endpoint}')
            except requests.exceptions.HTTPError as errh:
                print("Http Error:", errh)
            except requests.exceptions.ConnectionError as errc:
                print("Error Connecting:", errc)
            except requests.exceptions.Timeout as errt:
                print("Timeout Error:", errt)
            except requests.exceptions.RequestException as err:
                print("OOps: Something Else", err)
        elif method == 'post':
            try:
                response = requests.post(url=f'{base_url}{endpoint}', json=json_data)
            except requests.exceptions.HTTPError as errh:
                print("Http Error:", errh)
            except requests.exceptions.ConnectionError as errc:
                print("Error Connecting:", errc)
            except requests.exceptions.Timeout as errt:
                print("Timeout Error:", errt)
            except requests.exceptions.RequestException as err:
                print("OOps: Something Else", err)
        elif method == 'delete':
            try:
                response = requests.get(url=f'{base_url}{endpoint}')
            except requests.exceptions.HTTPError as errh:
                print("Http Error:", errh)
            except requests.exceptions.ConnectionError as errc:
                print("Error Connecting:", errc)
            except requests.exceptions.Timeout as errt:
                print("Timeout Error:", errt)
            except requests.exceptions.RequestException as err:
                print("OOps: Something Else", err)
        return response

    @staticmethod
    def get_value(gen_object: list):
        for value in gen_object:
            yield value
