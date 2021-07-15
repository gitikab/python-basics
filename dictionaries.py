# Dictionary is a collection of key and value pairs

# Creating a dictionary
country_capitals = {"France": "Paris", "Italy": "Rome",
                    "UK": "London", "Scotland": "Edinburgh",
                    "Germany": "Berlin", "Netherlands": "Amsterdam"}

# Accessing a value
print(country_capitals["Scotland"])

# Adding a new key value
country_capitals["Austria"] = "Vienna"

print(country_capitals)

# Modify a value in dictionary
country_capitals["Scotland"] = "Glasgow"
print(country_capitals)

# Removing key value pair
del country_capitals["Austria"]
print(country_capitals)

# Looping through all keys and their values
for country in country_capitals:
    print(country_capitals[country] + " is the capital of " + country)
print("\n")
for country in country_capitals.keys():
    print(country_capitals[country] + " is the capital of " + country)
print("\n")

# Looping through keys and values
for country, capital in country_capitals.items():
    print(capital + " is the capital of " + country)

# Looping through values
for capitals in country_capitals.values():
    print(capitals)

# Looping through unique values
for capitals in set(country_capitals.values()):
    print(capitals)

if "Austria" not in country_capitals.keys():
    print("Austria is missing")

# Sorted order
for country in sorted(country_capitals.keys()):
    print(country)

# List of dictionaries
student_1 = {"firstname": "Gitika", "lastname": "Bansal"}
student_2 = {"firstname": "Alka", "lastname": "Jhawar"}
student_3 = {"firstname": "Shifali", "lastname": "Jindal"}
student_4 = {"firstname": "Somya", "lastname": "Verma"}
students = [student_1, student_2, student_3, student_4]

for student in students:
    for key in student:
        print(student[key])

# List in a dictionary
country_rivers = {
    "India": ["Ganga", "Yamuna", "Brahmaputra"],
    "Pakistan": ["Jhelum", "Beas"]
}

for country in country_rivers:
    print(country + " has following rivers:")
    for river in country_rivers[country]:
        print(river)

# Dictionary in a dictionary
continents = {
    "Asia": {"India": "New Delhi", "China": "Beijing"},
    "Europe": {"France": "Paris", "Germany": "Berlin"}
}

for continent in continents:
    print(continent + " has following countries:")
    for country, capital in continents[continent].items():
        print(country + ", whose capital is " + capital)

