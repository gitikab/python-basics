import json

try:
    with open("username.txt") as user:
        username = json.load(user)
except FileNotFoundError:
    username = input("Please enter your name: ")
    print("Hii " + username)
    remember_me = input("Do you want me to remember you?: ")
    if remember_me.lower() == 'yes':
        with open("username.txt", 'w') as user:
            json.dump(username, user)
else:
    print("Welcome back " + username)
