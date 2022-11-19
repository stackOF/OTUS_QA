class DogAPI:
    """Данные для Dog API"""
    BASE_URL = 'https://dog.ceo/api/'
    ALL_BREEDS = 'breeds/list/all'
    MULTIPLE_IMAGES_FORM_A_BREED = 'breeds/image/random/'
    SINGLE_RANDOM = 'breeds/image/random'

    SOME_TRUE_BREEDS_LIST = ["boxer", "pug", "saluki"]
    FAKE_BREED_LIST = ["Pig", "Boxer1"]


class BreweryAPI:
    """Данные для Brewery API"""
    BASE_URL = 'https://api.openbrewerydb.org/breweries/'
    RANDOM_BREWERY = 'random'
    FILTER_BY_CITY = '?by_city'
    FILTER_BY_SORT_OF_BREWERY = '?by_type'
    PER_PAGE = '?per_page='

    TYPE_OF_BREWERY = ["nano", "micro", "regional", "brewpub", "large", "planning", "bar", "contract", "closed"]


class JSONPLaceholderAPI:
    """Данные для jsonplaceholder"""
    BASE_URL = 'https://jsonplaceholder.typicode.com/'
    POSTS = 'posts'
    DELETE_POST = 'posts/'

    DATA_FOR_POST = {
        'title': 'Breaking news!',
        'body': 'The older the person, the older he is',
        'userId': 5
    }
