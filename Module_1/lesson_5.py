# What is a String Method?
# A method is a function that belongs to an object.
# Think of a string as a smartphone.
# The phone(string) has apps (methods):
# Camera
# Calculator
# Gallery
# Similarly, a string has methods like:
# .upper()
# .lower()
# .replace()
# .find()


# 1. upper()
# Converts all letters to uppercase.

# name = "Abhishek"

# print(name.upper())

# 2. lower()
# Converts all letters to lowercase.

# name = "AbHiShEK"
# print(name.lower())


# 3. capitalize()
# Capitalizes only the first letter.

# text = "python"

# print(text.capitalize())


# title()
# Capitalizes the first letter of every word.

# course = "cloud computing"

# print(course.title())


# strip():
# Removes spaces from the beginning and end.

# name = "   Abhishek    "
# print(name.strip())

# There are also:

# text = "    Python    "

# print(text.lstrip())  # Remove left spaces
# print(text.rstrip())  # Remove right spaces


# 6. replace()
# Replaces one part of a string with another.

# sentence = "I like Java"

# print(sentence.replace("Java", "Python"))


# 7. find()
# Returns the index of the first occurrence.

# word = "Programming"

# print(word.find("g"))

# # If the text isn't found:
# print(word.find("z"))    # -1

# 8. count()
# Counts how many times something appears.

# word = "Programming"
# print(word.count("m"))


# 9. startswith()
# Checks if a string starts with something.
# email = "abc@gmail.com"

# print(email.startswith("abc"))


# 10. endswith()
# Checks if a string ends with something.

# email = "abc@gmail.com"
# print(email.endswith(".com"))


# 11.split()
# Splits a string into a list.

# sentence = "Python is awesome"

# words = sentence.split()

# print(words)


# date = "09-07-2026"

# print(date.split("-"))


# 12. join()
# Joins a list into a string.

# words = ["I", "love", "Python"]

# # sentence = " ".join(words)

# print(" ".join(words))

# Strings are Immutable:
# Methods like .upper() don't change the original string.

name = "Abhishek"
name.upper()
print(name)

# Why?
# Because .upper() returns a new string.
# To save the change:
name = name.upper()
print(name)









