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
    print("Type 'r' for rock, 'p' for paper or 's' for scissor") 
    user = input("Otherwise type 'e' to exit: ")
    if user == 'e':
        break
    if user not in ['r', 'p', 's']:
        print("Your input is invalid! ", end = "")
        continue
    pc = random.choice(['r', 'p', 's'])

    if user == pc:
        print("It's a tie! PC choose also " + pc + '\n')
        continue
    if (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
        print("You won! PC chose " + pc + '\n')
    else:
        print("You lost. PC chose " + pc + '\n')