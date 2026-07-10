# Exercise 1

name = "python programming"

print(name.upper())         # Uppercase
print(name.lower())         # Lowercase
print(name.title())         # Title Case
print(name.capitalize())    # Capitalized



# Exercise 2

text = "    Hello World    "

print(text)                # Original text
print(text.strip())        # Removes spaces from both sides
print(text.lstrip())       # Removes space from left side
print(text.rstrip())       # Removes space from right side



# Exercise 3

sentence = "I love Java"

print(sentence.replace("Java", "Python"))



# Exercise 4

word = "Mississippi"

print(word.count("s"))
print(word.count("i"))
print(word.count("p"))
print(word.count("z"))


# Exercise 5

email = "student@gmail.com"

print(email.startswith("student"))
print(email.endswith(".com"))
print(email.endswith(".org"))



# Exersice 6

sentence = "Python is easy to learn"

words = sentence.split()

print(words)

print(" ".join(words))