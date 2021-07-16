# Defining a function
def greet():
    print("Hello !!")


greet()


# Passing information to a function
def greet_user(username):
    print("Hello " + username + " !!")


greet_user("Gitika")


def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type)
    print("The " + animal_type + "'s name is " + pet_name)


# Positional Arguments
describe_pet("cat", "Annie")

# Keyword Arguments
describe_pet(pet_name="Annie", animal_type="cat")

# Combination
describe_pet("cat", pet_name="Annie")


# Default arguments - should always come last
def describe_your_pet(pet_name, animal_type="cat"):
    print("I have a " + animal_type)
    print("The " + animal_type + "'s name is " + pet_name)


describe_your_pet("Kittu")


# Argument Errors - TypeError when less or more than required number of parameters are passed
# describe_your_pet()
# describe_your_pet("cat", "Kitty", "Kittu")


# Returning values from functions
def greeting(username):
    return "Hello " + username + " !!"


message = greeting("Annie")
print(message)


# Making arguments optional
def full_name(firstname, lastname, middlename=""):
    if middlename:
        print(firstname + " " + middlename + " " + lastname)
    else:
        print(firstname + " " + lastname)


full_name("Gitika", "Sinha", "Ajitesh")
full_name("Gitika", "Bansal")


# Returning a dictionary
def build_person(firstname, lastname):
    return {"firstname": firstname, "lastname": lastname}


person = build_person("Ajitesh", "Sinha")
print(person)


# Passing a list as argument
def greet_users(users):
    for user in users:
        print(" Hi " + user)


greet_users(["Harry", "Ron", "Hermione"])


# Modifying list in a function
def process_task(tasks):
    while tasks:
        print(tasks.pop() + " is done")


pending_tasks = ["Cooking", "Laundry", "Cleaning"]
print(pending_tasks)
process_task(pending_tasks)
print(pending_tasks)

# Prevent function from modifying list - pass a copy of the original list
to_do = ["Bathing", "Studying", "Shopping"]
print(to_do)
process_task(to_do[:])
print(to_do)


# Variable Args - should be the last argument
def make_pizza(*toppings):
    for topping in toppings:
        print("Put " + topping + " on my pizza")


make_pizza("Tomato")
make_pizza("Tomato", "Basil", "Cheese")


# Ordering different types of arguments
def make_pasta(pasta_type, *toppings, sauce_type="white"):
    topping_string = " ".join(toppings)
    print("I want a " + pasta_type + " pasta in " + sauce_type + " sauce with " + topping_string)


make_pasta("sphagetti", "olives", "broccoli")
make_pasta("sphagetti", "olives", "pepper", sauce_type="red")


# Using arbitrary keyword arguments
def make_profile(firstname, lastname, **user_info):
    print("I am "+ firstname + " " + lastname)
    for key, value in user_info.items():
        print("My " + key + " is " + value)


make_profile("James", "Cameron", birthday="3rd June", hobby="Sketching")
