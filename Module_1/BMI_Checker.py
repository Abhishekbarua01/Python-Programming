# 🌟 Mini Project: BMI Checker

# Ask the user for:

# Weight (kg)
# Height (meters)

# Calculate BMI:

# bmi = weight / (height ** 2)

# Then classify:

# BMI	                Category
# Less than 18.5	   Underweight
# 18.5 to 24.9	         Normal
# 25 to 29.9	        Overweight
# 30 or above	        Obese


weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(meters): "))

bmi = weight / (height ** 2)


if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")