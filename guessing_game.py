"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    name = input("Hey welcome to the number guessing game. Whats your name?  ")
    random_number = random.randint(1, 10)
    attempt = 0
    
    while True:
        player_guess = input("Hey {}, guess the random number between 1 through 10:  ".format(name))
        #checking if its an int
        try:
            player_guess = int(player_guess)
        except ValueError:
            print("Pleas enter a valid number 1 through 10")
            continue
        #checking if it is within range
        if player_guess < 1 or player_guess > 10:
            print("{} please enter a number between 1 and 10".format(name))
            continue
        #tracking how many guesses
        attempt += 1
        
        if player_guess > random_number:
            print("It's lower, guess again {}".format(name))
        elif player_guess < random_number:
            print("It's greater, guess again {}".format(name))
        else:
            print("Got it, the number was {}".format(random_number))
            print("It took you {} guesses...".format(attempt))
            print("Bye {}, Thanks for playing!!!".format(name))
            break

# Kick off the program by calling the start_game function.
start_game()