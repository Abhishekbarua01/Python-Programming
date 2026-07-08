# Mini Project - Simple Calculator

# Create a calculator that:
# Asks the user for two numbers.
# Displays:
# Addition
# Subtraction
# Multiplication
# Division
# Modulus
# Floor Division
# Exponent

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number:"))

# print("Addition:", num1 + num2)
# print("Subtraction:", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Division:", num1 / num2)
# print("Modulus:", num1 % num2)
# print("Floor division:", num1 // num2)
# print("Exponent:", num1 ** num2)


print("=" * 30)
print("Welcome to Simple Calculator")
print("=" * 30)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} + {num2} / 2 = {(num1 + num2) / 2}")

