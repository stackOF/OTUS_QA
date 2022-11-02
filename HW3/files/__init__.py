import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename):
    return os.path.join(FILES_DIR, filename)


JSON_USER = get_path(filename='users.json')
CSV_BOOKS = get_path(filename='books.csv')
JSON_RESULT = get_path(filename='result.json')
