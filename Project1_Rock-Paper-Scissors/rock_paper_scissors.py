# This is a python code to play rock, paper, scissors game between the user and PC.

# Pseudo code:
# start the game
# user input choice 
# PC random choice
# compare user and pc choices
# if tie -> repeat
# else: user win if (user = p and PC = r) or (user = r and PC = s) or (user = s and PC = p)
# else: PC win

import random

def user_choice():
    """
    Function to get user input for Rock, Paper, Scissors game.

    Returns:
    str: User's choice ('r', 'p', 's', or 'e' to exit).
    """
    print("Type 'r' for rock, 'p' for paper, or 's' for scissor")
    return input("Otherwise type 'e' to exit: ")

# Main game loop
print("Welcome to Rock, Paper, Scissors game")
while True:
    # Get user's choice
    user = user_choice()

    # Check for exit condition
    if user == 'e':
        break

    # Validate user input
    if user not in ['r', 'p', 's']:
        print("Your input is invalid! ", end="")
        continue

    # Generate computer's choice
    pc = random.choice(['r', 'p', 's'])

    # Determine the winner and print the result
    if user == pc:
        print(f"####      It's a tie! PC also chose {pc}    ####\n")
    elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
        print(f"####      You won! PC chose {pc}            ####\n")
    else:
        print(f"####      You lost. PC chose {pc}           ####\n")
