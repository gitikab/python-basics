# Using range function to generate lists of numbers
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# First 10 squares
squares = []
for number in range(1, 11):
    squares.append(number**2)
print(squares)

digits = list(range(0, 10))
print(min(digits))
print(max(digits))
print(sum(digits))
