# Sorting a list permanently
flowers = ["jasmine", "rose", "marigold", "tulips", "lily"]
print(flowers)
flowers.sort()
print(flowers)
flowers.sort(reverse=True)
print(flowers)

# Sorting a list without affecting the original list
flowers = ["jasmine", "rose", "marigold", "tulips", "lily"]
print(flowers)
print(sorted(flowers))
print(flowers)
print(sorted(flowers, reverse=True))
print(flowers)

# Reversing a list permanently
print(flowers)
flowers.reverse()
print(flowers)

# Length of a list
print(len(flowers))

# IndexError when accessing index that doesn't exist
# flowers[5]

# Use last index instead
print(flowers[-1])

# Accessing last element can also return IndexError if list is empty
empty_list = []
#empty_list[-1]

# Search in a list
index_of_rose = flowers.index("rose")
print(index_of_rose)

# Membership test
print("rose" in flowers)





