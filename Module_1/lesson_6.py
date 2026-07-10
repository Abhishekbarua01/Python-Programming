# Conditional Statements (if, elif, else)

# What is a Conditional Statement?
# A conditional statement allows your program to make decisions based on whether a condition is True or False.
# Real-life Example

# Imagine you're going to watch a movie.

# If you have a ticket → Enter the theater.
# Otherwise → Buy a ticket first.

# This is exactly how an if statement works.


# Boolean Expressions:
# A condition always evaluates to either: True or False 
# Example:

print(10 > 5)   # True

# Another example:

print(20 < 10)    # False


# The if Statement 
# Syntax
# if condition:
    # code

# Example

age = 20

if age >= 18:
    print("You are eligible to vote.")


# If the condition is False, nothing inside the if block runs.


# Understanding Indentation 
# Python uses indentation (spaces) to define blocks of code.

# Correct way:
age = 20 

if age >= 18:
    print("Eligible for driving license.")


# Incorrect way:
# age = 20 

# if age >= 18:
# print("Eligible")

# This produces: IndentationError

# Best practice: Use 4 spaces for each indentation level.
# Most editors (like VS Code) do this automatically.


# The if...else Statement
# When there are two possible outcomes.

# Syntax:

# if condition:
    # True block
# else:
    # False block


# Example:
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")


# The if...elif...else Statement
# Used when there are multiple conditions.

# Syntax:
# if condition:
    # code block
# elif condition:
    # code block
# elif condition:
    # code 
# else:
    # code


# Example:

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# Important Note:
# Python checks conditions from top to bottom.
# As soon as one condition is True, the remaining conditions are skipped.



# Nested if
# An if statement inside another if.

# Example:

age = 22
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a driving license.")
else:
    print("You are too young to drive.")


# Using and:
# Both conditions must be True.

age = 22
salary = 20000

if age >= 18 and salary >= 30000:
    print("Loan Approved!")


# Using or:
# At least one condition must be True.

has_ticket = False
is_vip = True

if has_ticket or is_vip:
    print("Entry Allowed")



# Using not:
# Reverses a Boolean value.

logged_in = False

if not logged_in:
    print("Please log in.")




# Real-world Example 1: Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")



# Real-World Example 2: Password Check

password = input("Enter password: ")

if password == "Python123":
    print("Access Granted")
else:
    print("Incorrect Password")


# Real-World Example 3: Temperature

temperature = int(input("Enter temperature: "))

if temperature > 35:
    print("It's very hot.")
elif temperature >= 20:
    print("The weather is pleasant.")
else:
    print("It's cold.")