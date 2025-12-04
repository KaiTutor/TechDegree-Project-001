"""
Python Web Development Techdegree
Project 1 - Number Guessing Game - KaiTutor
--------------------------------
"""

import random


def start_game():

    while True:
        name = input("Hey welcome to the number guessing game. Whats your name?  ")
        random_number = random.randint(1, 10)
        attempt = 0
        high_score = None
    
        #loop for guessing number
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
                break

        if high_score is None or attempt < high_score:
            high_score = attempt
            print("Current High Score: {}".format(high_score))

        play_again = input("{}, would you like to play again?\nEnter Yes/No:   ".format(name))
        if play_again.lower() == "no":
            print("Bye {}, Thanks for playing!!".format(name))
            break



start_game()
