# Exercise 1
#  convert the folloewing: "25" to an integer and print its type.

age = int("25")
print(age)
print(type(age))

# # Convert into a float. 50

weight = float(50)
print(weight)
print(type(weight))



# # Convert 99 into a string.

age = 99
print("age: " + str(age))
print(type(age))


# Predict the output before running the code:

print(bool(0))  # False
print(bool(10))  # True
print(bool(""))  #False
print(bool("Hello"))  #True




# Exercise 5

# Ask the user for:
# Name
# Age
# Height
# Store them with the appropriate data types, then print:


print("Student Information")
print("-" * 20)

name = str(input("Name: "))
age = int(input("Age: "))
height = float(input("Height: "))
print(name)
print(age)
print(height)


# Bonus Challenge
# Ask the user for two numbers as input.
# Print:
# Sum
# Average
# Product

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum: ", num1 + num2)
print("Average: ", (num1 + num2) / 2)
print("Product: ", num1 * num2)
