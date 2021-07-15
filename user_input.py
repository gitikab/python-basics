# Taking user input

message = input("Tell me something and i will repeat it to you!!")
print(message)

name = input("Please enter your name: ")
print("Hello " + name + "!!")

# Accepting numerical input
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("Congratulations!! You can vote.")
else:
    print("Sorry!! You can't vote.")

# Modulo operator - returns the remainder
number = input("Enter a number and i will tell you if it is odd or even! ")
if int(number) % 2 == 0:
    print(number + " is even")
else:
    print(number + " is odd")
