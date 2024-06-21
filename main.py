# Write a program that tests your ESP (extrasensory perception).
# The program should randomly select the name of a color from the following list:
# Red, Green, Blue, Orange, Yellow

# To select a word, the program can generate a random number.
# For example, if the number is 0, the selected word is Red.
# If the number is 1, the selected word is Green, and so forth.

# Next, the program should ask the user to enter the color that the computer has selected.
# After the user has entered their guess, the program should display the name of the randomly selected color.
# The program should repeat this 10 times and then display the number of times the user correctly guessed the selected color.

# import the random module
import random

# variables
correct_guesses = 0

print("Hey Tatiana! Can you guess which color the computer chose?\n(Red, Green, Blue, Orange, Yellow)\n")

# use the random.randint() method to generate a random integer within the given range
for iteration in range(10):
    number = random.randint(0,4)
    
    # equate the number the program randomly selected to one of the colors given
    if (number == 0):
        color = "red"
    elif (number == 1):
        color = "green"
    elif (number == 2):
        color = "blue"
    elif (number == 3):
        color = "orange"
    else:
        color = "yellow"
 
    # ask the user to guess which color the computer selected
    user_guess = input(f"Guess {iteration + 1}: ").lower()
    
    # input validation
    while (user_guess != "red" and user_guess != "green" and user_guess != "blue" and user_guess != "orange" and user_guess != "yellow"):
        user_guess = input(f"Sorry, that is not one of the color options. Please try again. Guess {iteration + 1}: ").lower()
 
    # display the color that corresponds to the number that the program randomly selected
    print(f"The computer chose {color}!\n")

    # keep track of the number of correct guesses
    if (user_guess == color):
        correct_guesses += 1

print(f"Thanks for playing! You got {correct_guesses} guess(es) correct.")