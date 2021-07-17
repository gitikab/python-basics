import json


def get_stored_username():
    try:
        with open("username.txt") as stored_user:
            return json.load(stored_user)
    except FileNotFoundError:
        return None


def get_new_username():
    return input("Please enter your name: ")


def store_username(user_name):
    with open("username.txt", 'w') as user:
        json.dump(user_name, user)


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome Back " + username)
    else:
        username = get_new_username()
        store_username(username)
        print("Hi " + username)


greet_user()
