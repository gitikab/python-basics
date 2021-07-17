# Handle specific error
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Handle all errors
try:
    print(5 / 0)
except:
    print("Error Occurred")

# Else
try:
    answer = 5 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(answer)

# Failing silently
try:
    answer = 5 / 2
except ZeroDivisionError:
    pass
else:
    print(answer)
