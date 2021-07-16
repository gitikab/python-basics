# String data type
string_using_single_quotes = 'This is a string'
print(string_using_single_quotes)
string_using_double_quotes = "This is also a string"
print(string_using_double_quotes)

# Using quotes and apostrophes in strings
first = 'I told my friend, "Python is my favorite language"'
print(first)
second = "I am visiting my friend's house in the afternoon"
print(second)
third = "The language 'Python' is not named after a snake"
print(third)

# Changing string case
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Concatenating strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello " + full_name.title() + "!")
message = "Hello " + full_name.title() + "!"
print(message)

# Adding whitespace using tabs and newlines
print("Python")
print("\tPython")
print("Languages:\nJava\nC\nPython\nGolang")
print("Languages:\n\tJava\n\tC\n\tPython\n\tGolang")

# Stripping whitespace
favorite_language = "Python "
print(favorite_language.rstrip())
print(favorite_language)

favorite_language = " Python"
print(favorite_language.lstrip())
print(favorite_language)

favorite_language = " Python "
print(favorite_language.strip())
print(favorite_language)

# Using single quotes to create a string containing a single quote throws SyntaxError
# message = 'One of Python's strengths is its diverse community.'


