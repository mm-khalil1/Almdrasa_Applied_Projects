import random

def get_user_choice():
    """
    Function to get user input for Rock, Paper, Scissors game.

    Returns:
    str: User's choice ('r', 'p', 's', or 'e' to exit).
    """
    print("Type 'r' for rock, 'p' for paper, or 's' for scissor")
    return input("Otherwise type 'e' to exit: ")

def get_computer_choice():
    """
    Function to randomly generate the computer's choice for Rock, Paper, Scissors game.

    Returns:
    str: Computer's choice ('r', 'p', 's').
    """
    return random.choice(['r', 'p', 's'])

def determine_winner(user, pc):
    """
    Function to determine the winner of the Rock, Paper, Scissors game.

    Args:
    user (str): User's choice ('r', 'p', 's').
    pc (str): Computer's choice ('r', 'p', 's').

    Returns:
    str: Result message indicating the outcome of the game.
    """
    if user == pc:
        return "It's a tie! PC chose also " + pc
    if (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
        return "You won! PC chose " + pc
    else:
        return "You lost. PC chose " + pc

# Main game loop
print("Welcome to Rock, Paper, Scissors game")

while True:
    # Get user's choice
    user_choice = get_user_choice()

    # Check for exit condition
    if user_choice == 'e':
        break

    # Validate user input
    if user_choice not in ['r', 'p', 's']:
        print("Your input is invalid! ", end="")
        continue

    # Generate computer's choice
    computer_choice = get_computer_choice()

    # Determine the winner and print the result
    result = determine_winner(user_choice, computer_choice)
    print(result + '\n')
