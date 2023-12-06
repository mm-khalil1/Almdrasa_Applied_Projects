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

print("Welcome to Rock paper scissors game")
game = 1
while (game != 'e'):
    user = input("Type 'r' for rock, 'p' for paper or 's' for scissor. Or 'e' to end the game: ")
    if user not in ['r', 'p', 's']:
        user = input("Your input is invalid. Type r, p or s: ")
    pc = random.choice(['r', 'p', 's'])

    if user == pc:
        print("It's a tie! PC choose also " + pc)
        continue
    if (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
        print("You won! PC chose " + pc)
    else:
        print("You lose. PC chose " + pc)