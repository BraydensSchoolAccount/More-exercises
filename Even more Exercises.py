# Python Exercises 2: Electric Boogaloo
# Brayden Towner
# 10/30/2023

import os
exercise_int=1

# Just to keep it in one file, I'll use headers and cls to clarify exercises.
# This code repeats a lot
def next_exercise(exercise_name):
    # It tries to grab the local variable with this name which doesn't exist...
    # I knew of this keyword already
    global exercise_int
    # Only pause pre-exercise if this isn't the first
    if exercise_int > 1:
        os.system("pause")
    os.system("cls")
    print(f"Exercise {exercise_int}: {exercise_name}\n")
    exercise_int+=1


next_exercise("Deep... (crying pepe emoji)")

quote = "In place of death, there was light"

# Use strings being arrays to our advantage by splicing them like arrays
print(f"The first 5 characters of it are \"{quote[0:5]}\"")
print(f"Characters 10-15 are \"{quote[10:15]}\"")

next_exercise("\"I don't know much about my name...\"")

# Get users name
user_name = input("What is your name? >  ")

# This types the last 3 characters, and the empty colon starts it from the beginning of the string
# Unlike 0 for some reason
print(f"The last three characters of your name are \"{user_name[-3:]}\"")

next_exercise("You really don't")

first_name = input("What is first name? >  ")
last_name = input("What is last name? >  ")

full_name = f"{first_name} {last_name}"

print("HELLO",full_name.upper())
print(full_name.title())
print(full_name.lower())

next_exercise("Finding a python")

fact = "Every student can learn the Python language."

print(fact.find("Python"))

next_exercise("\t\t\t\t\tE")

print(f"There are {fact.count('e')} lowercase e's in {fact}")

next_exercise("Who puts sentences in bullet point format?!")

todo = ["Yo", "I", "see", "many", "bats", "flying", "around"]
print(" ".join(todo))