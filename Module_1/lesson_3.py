#  Type Casting in Python


# age = int(input("Enter your age: "))  # Convert the input to an integer.

# print(age + 5)


# Explicit Type Casting: When you tell Python to convert a value, it's called explicit type casting.

# num = int("100")  # int(): convert to an integer.
# print(num)
# print(type(num))  #<class 'int'>


# Float to Integer 

# num1 = int(10.5) # Convert float to integer
# print(num1)  # Output: 10
# print(type(num1))  #<class 'int'>


# Float(): Converts to a decimal number (float).

# num2 = float(10) # Convert integer to float
# print(num2) # Output: 10.0
# print(type(num2)) #<class 'float'>

# price = float("99.99") # Convert string to float
# print(price) # Output: 99.99
# print(type(price)) #<class 'float'>


# str(): Converts a value into a string.

# age = 21

# # text = str(age) # Convert integer to string
# # print(text) # Output: "21"
# # print(type(text)) #<class 'str'>

# print("Age: " + str(age)) # Concatenate string with integer after converting to string
# print(type(age)) #<class 'int'>

# print(f"Age: {age}") # Using f-string to include integer in string



# bool(): Converts a value to a boolean (True or False).

# print(bool(1)) # Output: True
# print(bool(0)) # Output: False
# print(bool("")) # Output: False
# print(bool("Hello")) # Output: True
# print(bool([])) # Output: False


# Implicit Type Casting: Sometimes Python converts types automatically.

num1 = 10
num2 = 2.5

add = num1 + num2

print(add)

print(type(add))



