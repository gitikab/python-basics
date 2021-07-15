cars = ["audi", "bmw", "subaru", "toyota"]

# Checking equality
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# Checking inequality
for car in cars:
    if car != 'bmw':
        print(car)

# Relational Operator
numbers = [1, 5, 25, 60, 3, 22]
for number in numbers:
    if number > 10:
        print(str(number) + " is greater than 10")
    elif number <= 30:
        print(str(number) + " is between 1 and 10")
    else:
        print(str(number) + " is greater than 30 or less than 10")

# Logical operator and or
for number in numbers:
    if number > 10 and number * 2 > 30:
        print(str(number) + " is a good number")
    else:
        print("I don't care about " + str(number))

# in operator
if 'bmw' in cars:
    print("bmw is present")

# not operator
if 'ferrari' not in cars:
    print("Ferrari is not present")

# check if a list is empty
cities = []
if cities:
    print(cities)
else:
    print("Cities is empty")



