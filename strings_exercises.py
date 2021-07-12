"""
Store a person’s name in a variable, and print a message to that person.
Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
"""
name = 'Gitika'
message = "Hello " + name + ", would you like to learn some Python today?"
print(message)

# Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
another_name = 'gitika bansal'
print(another_name.lower())
print(another_name.upper())
print(another_name.title())

# Find a quote from a famous person you admire. Print the quote and the name of its author.
famous_quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(famous_quote)

famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
famous_person_quote = famous_person + ' once said, "' + quote + '"'
print(famous_person_quote)

name_with_space_1 = "\tMonty "
print("*" + name_with_space_1 + "*")
print("*" + name_with_space_1.lstrip() + "*")
print("*" + name_with_space_1.rstrip() + "*")
print("*" + name_with_space_1.strip() + "*")
print("\n")

name_with_space_2 = "\nMonty "
print("*" + name_with_space_2 + "*")
print("*" + name_with_space_2.lstrip() + "*")
print("*" + name_with_space_2.rstrip() + "*")
print("*" + name_with_space_2.strip() + "*")
print("\n")

name_with_space_3 = " \nMonty\t "
print("*" + name_with_space_3 + "*")
print("*" + name_with_space_3.lstrip() + "*")
print("*" + name_with_space_3.rstrip() + "*")
print("*" + name_with_space_3.strip() + "*")
print("\n")

# strip functions remove whitespace, tabs and newlines
