with open("story.txt") as story:
    contents = story.read()
    print(contents)

with open("textfiles/another_story.txt") as another_story:
    print(another_story.read())

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
