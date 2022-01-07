# Strings are immutable sequences of characters

# Concatenate
s1 = "Hello "
s2 = "World!"
s3 = s1 + s2
print(s3)


# Repeat
blah = "Blah "
blabber = blah * 5
print(blabber)

# Indexing from front and back
word = "Mississippi"
fourth = word[4]
last = word[-1]
second_last = word[-2]
print(fourth, last, second_last)

# Slice from front and back
miss = word[0:4]
another_miss = word[:4]
sip = word[-5:-2]
print(miss, another_miss, sip)

# Length
length = len(word)
print(length)

# String Formatting
print("My name is %s, Hiii" % "Harry")
print("I am %s years old" % 11)
print("I am %s cm tall" % 150.50)
print("%s , %s and %s are best friends" % ("Harry", "Ron", "Hermione"))

# Iteration
for char in word:
    print(char + "\n")


# Membership
for char in word.lower():
    if char in "aeiou":
        print("%s is a vowel" % char)


# Changing string sequence throws TypeError as it is immutable so doesn't support assignment
# word[4] = "x"

