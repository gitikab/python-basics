# Tuple is an immutable list
fruits = ("apple", "mango", "banana", "grapes")
print(fruits[2])

for fruit in fruits:
    print(fruit)

# TypeError if a tuple value is changed
#fruits[0] = "Apple"

# No error if a tuple variable is reassigned
fruits = ("Pear", "Peach")

# All other tuple operations are same as list like indexing, slicing, searching, membership
