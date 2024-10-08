# 3.Rock, Paper, Scissors Game

# Concepts: Conditional statements, Loops, Random module
# Description: The user plays against the computer, selecting rock, paper, or scissors,
# and the program determines the winner based on the classic rules.

from random import randint
options = {1:'Rock',
           2:'Paper',
           3:'Scissors'}
while True:
    print("\nSelect any option: 1 for Rock, 2 for Paper, 3 for Scissors")
    try:
        user_selection = int(input("Enter your Choice: "))
        if user_selection not in options:
            print("Invalid Selection!")
            continue
    except ValueError:
        print("Enter the correct option")
        continue

    computer_choice= randint(1,3)
    print(f"computer choose: {options[computer_choice]}")
    print(f"You choosed : {options[user_selection]}")

    if computer_choice == user_selection:
        print("Its a Tie!!!")
    elif (user_selection == 1 or computer_choice == 3) or \
         (user_selection == 3 or computer_choice == 2) or \
         (user_selection == 2 or computer_choice == 1):
        print("You win the Game!!!")
    else:
        print("You Loose the Game!!")
    
    play_again = input("Do you want to paly again? (yes/no):").lower()
    if play_again != 'yes':
        break


