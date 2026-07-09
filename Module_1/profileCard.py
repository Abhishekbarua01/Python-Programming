# Mini Project - Profile Card

# Ask the user for:

# Name
# City
# Favorite Language


name = str(input("Enter your name: "))
city = str(input("Enter your city: "))
favorite_language = str(input("Enter your facorite language: "))

print("=" * 30)
print("PROFILE CARD")
print("=" * 30)

print(f"Name     : {name}")
print(f"City     : {city}")
print(f"Language : {favorite_language}")

print(f"First Letter : {name[0]}")
print(f"Last Letter : {name[len(name)-1]}")
print(f"Name Length : {len(name)}")