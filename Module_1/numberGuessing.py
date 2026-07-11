# 🌟 Mini Project – Number Guessing Game
# Write a program where:

# The secret number is:
# secret = 7
# Ask the user to guess the number.
# If the guess is correct:
# Congratulations! You guessed correctly.
# Otherwise:
# Try Again.
# ⭐ Bonus

# Keep asking until the user guesses correctly.

# (Hint: you'll need a while loop.)


# secret = 7

# guessNum = int(input("Guess the number: "))

# while guessNum != secret:
#     print("Try Again.")
#     guessNum = int(input("Guess the number: "))

# print("Congratulations! You guessed correctly.")



# Second version of this game

secret = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("🎉 Congratulatuions! You guessed correctly.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")