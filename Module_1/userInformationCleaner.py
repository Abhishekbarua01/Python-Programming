# 🌟 Mini Project – User Information Cleaner
# Ask the user for:

# Name
# Email
# City

# The user may enter values with extra spaces or mixed letter cases.

# Example input:

# Name :    abhishek
# Email :    ABC@GMAIL.COM
# City :    inDORE


name = str(input("Enter your name: ")).title()
email = str(input("Enter your email: ")).lower()
city = str(input("Enter your city: ")).capitalize()


print("=" * 30)
print("USER INFORMATION")
print("=" * 30)

print(f"\nName  : {name}")
print(f"Email : {email}")
print(f"City  : {city}")

print(f"Name Length : {len(name)}")
print(f"Email Ends With .com : {email.endswith(".com")}")