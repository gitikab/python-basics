# Reading a file in one go
with open("story.txt") as story:
    contents = story.read()
    print(contents)

# Relative path
with open("textfiles/another_story.txt") as another_story:
    print(another_story.read())

# Reading a file line by line
word_count = {}
with open("story.txt") as story:
    for line in story:
        words = line.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

for word, times in word_count.items():
    print(word + " occurs " + str(times) + " times")


# Reading a file into a list of lines
with open("story.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())


