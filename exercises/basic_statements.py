# Write a for loop to print the ASCII code of each character in a string
string_for_ascii_conversion = "My cat's name is Annie"
for char in string_for_ascii_conversion:
    print("%s -> %s" % (char, ord(char)))


# Change the above loop to calculate the sum of ascii values
sum = 0
for char in string_for_ascii_conversion:
    sum += ord(char)
print("The sum of ascii values is %s" % sum)

# Return a new list containing the ascii values
ascii_values = []
for char in string_for_ascii_conversion:
    ascii_values.append(ord(char))
print(ascii_values)
print(list(map(ord, string_for_ascii_conversion)))

# Print a dictionary's items in sorted order
country_capitals = {
    "New Zealand": "Auckland",
    "China": "Beijing",
    "Turkey": "Istanbul",
    "India": "New Delhi"
}

for country in sorted(country_capitals.keys()):
    print("%s -> %s" % (country, country_capitals[country]))

# Refactor below code
L = [2 ** i for i in range(0, 10)]
X = 5
value_to_search = 2 ** X
if value_to_search in L:
    print('at index', L.index(value_to_search))
else:
    print(X, 'not found')


