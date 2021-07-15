# Simple while loop
current = 1
while current < 10:
    print(current)
    current += 1

# User input in a while loop
prompt = "Tell me something and ! will repeat it back to you!!\nEnter quit to exit: "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Using a flag
active = True
while active:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        active = False

# Breaking out of a loop
while True:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        break

# Using continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# while loop with list - moving items from one list to another
source = ["1", "2", "3"]
destination = []
while source:
    destination.append(source.pop())
print(destination)

# Removing all instances of an item
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling dictionary with user input
favorite_city_poll = {}
while True:
    name = input("Please Enter your Name: ")
    favorite_city = input("Which is your favorite city: ")
    favorite_city_poll[name] = favorite_city
    repeat = input("Would anyone else like to do the poll? Yes/No? ")
    if repeat.lower() == 'no':
        break
