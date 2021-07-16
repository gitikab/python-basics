cities_travelled = ["Paris", "Versailles", "Venice", "Naples", "Sorrento", "Capri", "Positano",
                    "Pompeii", "Rome", "London", "Edinburgh", "Glasgow", "Oxford", "Cambridge",
                    "Brighton", "Amsterdam", "Berlin", "Salzburg", "Halstatt", "Vienna"]

# Slicing a list - start and end index excluding end index
print(cities_travelled[0:5])

# Slicing a list from start to given index
print(cities_travelled[:7])

# Slicing a list from given index to end
print(cities_travelled[7:])

# last 3 cities
print(cities_travelled[-3:])

# Looping through a slice
for city in cities_travelled[5:10]:
    print(city)

# Copying a list
cities_travelled_copy = cities_travelled[:]
cities_travelled_copy.append("Pune")
print(cities_travelled)
print(cities_travelled_copy)

# This is not copy
cities_travelled_reference = cities_travelled
cities_travelled_reference.append("Mumbai")
print(cities_travelled_reference)
print(cities_travelled)



