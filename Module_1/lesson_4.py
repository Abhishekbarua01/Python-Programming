# What is a String?
# A string is a sequence of characters enclosed in quotes.
# Examples:

name = "Abhishek"
city = "Indore"
course = "Cloud Computing"
email = "abc@gmail.com"

# Everthing inside the quotes is a string.


# Creating Strings:
# You can use either double quotes("") or single quotes('').

# name = "Abhishek"
# city = 'Indore'

# print(f"Name : {name}")
# print(f"City : {city}")

# What is a Character?
# A string is made up of individual characters.
# Example: Python
# It consists of:  P   y   t   h   o   n
# There are 6 characters.


# String Indexing:
# Each character has a position called an index.
# P   y   t   h   o   n
# 0   1   2   3   4   5

# Example:

# language = "Python"
# print(language[0])
# print(language[1])
# print(language[2])
# print(language[3])
# print(language[4])
# print(language[5])


# Positive Indexing:
# Positive indexing starts from 0.

# String:   H   e   l   l   o
# Index:    0   1   2   3   4

# word = "Hello"

# print(word[0])
# print(word[1])
# print(word[4])


# Negative Indexing:
# Negative indexing starts from the end.

# String:    P   y   t   h   o   n
# Index:    -6  -5  -4  -3  -2  -1

# word = "Python"
# print(word[-1])
# print(word[-2])


# why is Negative Indexing Useful?
# Suppose you always want the last character of a string.
# Instead of calculating:
# word[5]
# you can simply write:
# word[-1]
# This works no matter how long the string is.
# Example:

# name = "Abhishek"
# print(name[-1])

# Finding the Length of a String:
# Use the built-in len() function.

# language = "Python"

# print(len(language))

# name = "Abhishek"

# print(len(name))


# This shows why len() is useful--it avoids mistakes when counting manually.


# String Slicing:
# Slicing lets you extract part of a string.
# Syntax:
# string[start:end]
# start is included.
# end is excluded.

# word = "Python"
# print(word[0:2])

# Explanation:
# P   y   t   h   o   n
# 0   1   2   3   4   5
# Strat at index 0 and stop before index 2.

# # Another example:
# print(word[2:5])

# # From the beginning:
# print(word[:4])

# # Python assumes the start is 0.


# # Until the end:
# print(word[2:])
# # Python assumes the end is the last character.


# # Copy the whole string:
# print(word[:])


# String Immutability:
# String are immutable, which means you cannot change an individual character.

# This will cause an error:
# word = "Python"

# word[0] = "j"

# print(word)

# To create a modified string, build a new one:

word = "Python"

new_word = "J" + word[1:]

print(new_word)





