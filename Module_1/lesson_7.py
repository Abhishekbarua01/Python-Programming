# What is a loop?
# A loop is used to repeat a black of code multiple times.

# Real-Life Example
# Imagine your teacher asks you to write.
# I will practice Python.
# 10 times.
# Without a loop:
# print("I will practice Python.")
# print("I will practice Python.")
# print("I will practice Python.")
# print("I will practice Python.")
# print("I will practice Python.")
# print("I will practice Python.")
# print("I will practice Python.")
# print("I will practice Python.")
# print("I will practice Python.")
# print("I will practice Python.")

# This works, but it's repetitive.
# with a loop:
# for i in range(10):
#     print("I will practice Python.")
# Much shorter, easier to read, and easier to maintain.

# Types of Loops 
# Python provides two main loops.
# 1. for loop
# 2. while loop


# The for Loop
# Syntax:

# for variable in sequence:
    # code to repeat


# Example:

# for i in range(5):
#     print(i)
  

# Understanding range()
# The range() function generates a sequence of numbers.

# range(stop)

# for i in range(5):
#     print(i)


# Notice that 5 is not included.

# range(start, stop)

# for i in range(2, 6):
#     print(i)


# range(start, stop, step)

# for i in range(2, 11, 2):
#     print(i)


# The third value (2) is the step size, meaning the loop increases by 2 each time.




# Printing a Name Multiple Times

# name = "Abhishek"

# for i in range(5):
#     print(name)




# Loop Through a String
# You can loop through each character in a string.

# name = "Python"

# for letter in name:
#     print(letter)


# Loop Through a List

# fruits = ["Apple", "Banana", "Mango"]

# for fruit in fruits:
#     print(fruit)




# The while Loop
# A while loop repeats as long as a condition is True.

# Syntax

# while condition:
    # code

# Example:

# count = 1

# while count <= 5:
#     print(count)
#     count += 1

# Understanding the Flow

# Step-by-step
# Initial value:
# count = 1
# Check:
# 1 <= 5
# True -> print 1
# Increase:
# count = 2
# Again:
# 2 <= 5
# True --> print 2
# This continues until:
# count = 6
# Now:
# 6 <= 5
# False --> loop stops.


# Infinite Loop

# count = 1

# while count <= 5:
#     print(count)



# What happens?
# The value of count never changes.
# The condition is always True.
# This creates an infinite loop, and the program never ends.

# Always update the loop variable inside a while loop when needed.



# break
# The break statement immediately exits the loop.

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# When i becomes 5, the loop stops completely.




# continue
# The continue statement skips the current iteration and moves to the next one.

# for i in range(6):
#     if i == 3:
#         continue
#     print(i)

# The number 3 is skipped.




# Nested Loops
# A loop inside another loop.

# Example:

# for i in range(3):
#     for j in range(2):
#         print(i, j)

# The inner loop runs completely for every iteration of the outer loop.



# Pattern Printing

# Example:

# for i in range(5):
#     print("*")



# Now a triangle:

for i in range(1, 6):
    print("*" * i)

# Notice how "*" * i repeats the * character i times.








