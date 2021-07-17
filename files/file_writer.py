# Writing to an empty file - open file in write mode
# File modes read-only r, write w, append a, read-write r+
with open("aboutme.txt", 'w') as file:
    file.write("I love Python\n")
    file.write("I also love Java\n")

lines = ["I love Python\n", "I love Java\n"]
with open("textfiles/aboutme.txt", 'w') as file:
    file.writelines(lines)

# Append to a file
with open("aboutme.txt", 'a') as file:
    file.write("I love to travel too\n")


