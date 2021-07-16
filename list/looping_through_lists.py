# Looping through an entire list

capital_cities_travelled = ["Paris", "Rome", "London",
                            "Edinburgh", "Amsterdam", "Berlin",
                            "Vienna"]
for city in capital_cities_travelled:
    print(city)
    print("I have been to " + city)

print("That's it !!!")

numbers = ["One", "Two", "Three"]

# Indentation Errors

# IndentationError: expected an indented block
#for number in numbers:
#print(number)

# Forgot to indent , doesn't result in error but incorrect output
for number in numbers:
    print(number)
print(number + " is a good number")

# Forgot colon after a loop - SyntaxError: invalid syntax
#for number in numbers
#    print(number)



