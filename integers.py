add = 2 + 3
print(add)

subtract = 100 - 35
print(subtract)

multiply = 12 * 5
print(multiply)

divide = 120 / 6
print(divide)

exponent = 4 ** 3
print(exponent)

expression = 2 + 5 * 3 - 5 / 5
print(expression)

expression_with_parenthesis = ((2 + 5) * 3 - 5) / 5
print(expression_with_parenthesis)

# Note that expression is promoted to a float if any of the operations return a float

# Concatenating integers with strings
age = 2
# Returns TypeError
# greeting = "Happy " + age + "nd Birthday!!"
greeting = "Happy " + str(age) + "nd Birthday!!"
print(greeting)
