# Exercise 1: Voting Eligibility

# Ask the user for their age.

# If the age is 18 or above, print:

# You are eligible to vote.

# Otherwise:

# You are not eligible to vote.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")





# Exercise 2: Positive, Negative, or Zero

# Ask the user for a number.

# Print whether it is:

# Positive
# Negative
# Zero



number = int(input("Enter a number: "))

if number >= 1:
    print("Positive")
elif number <= -1:
    print("Negative")
else:
    print("Zero")




# Exercise 3: Grade Calculator

# Ask the user for marks.

# Use this grading system:

# Marks	      Grade
# 90–100	    A
# 75–89	        B
# 60–74 	    C
# Below 60	    D



marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")





# Exercise 4: Largest Number

# Ask the user for two numbers.

# Print which one is larger.

# If they are equal, print:

# Both numbers are equal.



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is the largest number.")
elif num2 > num1:
    print(f"{num2} is the largest number.")
else:
    print("Both numbers are equal.")






# Exercise 5: Login Check
# username = "admin"
# password = "python123"

# Ask the user to enter both.

# If both match, print:
# Login Successful

# Otherwise:

# Invalid Username or Password


userName = input("Enter Username: ")
password = input("Enter password: ")

if userName == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Username or Password")
