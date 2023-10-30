# More Exercises
# Brayden Towner
# 10/27/2023

import os

# Just to keep it in one file, I'll use headers and cls to clarify exercises
os.system("cls")
print("Exercise 1: Hello!\n")

# Print Every Character in "Hello there" individually
# This makes it vertical
greeting = "Hello there"
for letter in greeting:
    print(letter)

# A pause so you actually can understand what happened before moving on
os.system("pause")
os.system("cls")
print("Exercise 2: Ca$h Money\n")

story_sentence = "A screaming comes across the sky"
# Replace every "s" with cash money ($)
cash_moneyed_sentence = story_sentence.replace("s", "$")
print(cash_moneyed_sentence)

os.system("pause")
os.system("cls")
print("Exercise 3: 3 3's (three's)\n")

concat_threes = "three"
# Using all methods of concatenation (+=, +, .join), make "three three three"
concat_threes += " " + " ".join([concat_threes, concat_threes])
print(concat_threes)
# The multiply method
print("three " * 3)

os.system("pause")
os.system("cls")
print("Exercise 4: Cut it off\n")

april_log = "It was a bright cold day in April, and the clocks were striking thirteen"

# Cuts from the beginning to where the first comma is
# Totally for adaptability and not because I can't count beyond 4
time_and_condition = april_log[0:april_log.find(",")]
print(time_and_condition)

os.system("pause")
os.system("cls")
print("Exercise 5: Texting but in terminal\nTherefore it's cool B)\n")

# Get the message being sent and to what user it's being sent to
message = input("What do you want to send? >  ")
receiver = input("And to who? >  ")

os.system("cls")

print(f"Yesterday, I wrote {message}. I sent it to {receiver}!")

os.system("pause")
os.system("cls")
print("Exercise 6: Strip. \nwait STRINGS I MEANT STRINGS-\n")

# Have we learned regex yet? *Checks notes*
# UUUUUUGGHH!!

bad_name = "$$John**"

