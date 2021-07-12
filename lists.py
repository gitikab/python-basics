# Creating lists
fruits = ["Apple", "Mango", "Grapes", "Papaya"]
print(fruits)

# Accessing elements - zero index based
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Accessing elements from the end of the list
print(fruits[-1])
print(fruits[-2])

# Using individual elements from a list
print("My favorite fruits is " + fruits[1])

# Modifying elements in a list
fruits[-1] = "Strawberry"
print(fruits)

# Appending elements at the end of a list
fruits.append("Peach")
print(fruits)

# Inserting elements at a position
fruits.insert(1, "Pear")
print(fruits)

# Removing elements from a list
del fruits[1]
print(fruits)

# Remove last element from list and return it
print(fruits.pop())
print(fruits)

# Remove element at index from list and return it
print(fruits.pop(2))
print(fruits)

# Remove item by value - first occurrence only
fruits.append("Apple")
print(fruits.remove("Apple"))
print(fruits)
