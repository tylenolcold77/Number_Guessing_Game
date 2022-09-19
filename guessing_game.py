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
    count = 0
    print("Welcome to the guess number game.")
    solution = random.randint(1,11)
    answer = int(input("enter the number:  "))
    while solution != answer:
      if solution < answer:
        print("It's lower.")
        answer = int(input("enter the number:  "))
      else:
        print("It's higher.")
        answer = int(input("enter the number:  "))
      count += 1
    print("Got it")
    print("You take {} times.".format(count))   
    print("Game over")
# Kick off the program by calling the start_game function.
start_game()
