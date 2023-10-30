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

print(f"\"{quote}\" is the quote")
# Use strings being arrays to our advantage by splicing them like arrays
print(f"The first 5 characters of it are \"{quote[0:5]}\"")
print(f"Characters 10-15 are \"{quote[10:15]}\"")

next_exercise("\"I don't know much about my name...\"")

# This code is a botch
# Get users name and add an extra character
user_name = input("What is your name? >  ") + " "

# The intuitive thing would be using 0 and -3. [-3:0], [0:-3] both return the wrong thing
print(f"The last three characters of your name are \"{user_name[-4:-1]}\"")