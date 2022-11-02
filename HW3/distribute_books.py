import json
from csv import DictReader
from files import JSON_USER, CSV_BOOKS, JSON_RESULT
import copy


def get_format_user_list(user_data):
    format_user = []
    format_keys = ["name", "gender", "address", "age"]
    tmp_user = {}
    with open(user_data, 'r') as f:
        users_json = json.load(f)
    for user in users_json:
        for keys in format_keys:
            tmp_user[keys] = user[keys]
        format_user.append(copy.deepcopy(tmp_user))
    return format_user


def get_format_book_list(book_data):
    format_keys = ["Title", "Author", "Pages", "Genre"]
    format_books = {}
    final_book_list = []
    with open(book_data, "r") as f:
        csv_reader = DictReader(f)
        for row in csv_reader:
            for keys in format_keys:
                format_books[keys] = row[keys]
            final_book_list.append(copy.deepcopy(format_books))
    return final_book_list


def distribute_books(users_list, books_list):
    num_users = 0
    for i in range(len(users_list)):
        users_list[i]["books"] = []
    for book in books_list:
        users_list[num_users]["books"].append(book)
        num_users += 1
        if num_users == len(users_list) - 1:
            num_users = 0
    return users_list


def write_result_json(source_file, result_json_file):
    with open(result_json_file, 'w') as f:
        f.write(json.dumps(source_file, indent=4))


books = get_format_book_list(CSV_BOOKS)
users = get_format_user_list(JSON_USER)
distribute_books_list = distribute_books(users, books)
write_result_json(distribute_books_list, JSON_RESULT)
