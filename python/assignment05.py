'''

Rock Paper Scissors

Create a program that emulates a rock, paper scissors game.

Prompt the user for a number between 1 and 3 (1=Rock, 2=Paper, or 3=Scissors)
Use the random number generator to generate a random number between 1 and 3
Play the game! If the user chose a value that will beat the computer generated value then tell them that they have won. Other wise tell the user that they have lost

'''

def rock_paper_scissors():
    import random
    user_choice = int(input("Choose 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    computer_choice = random.randint(1,3)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 1 and computer_choice == 3:
        print("You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    elif user_choice == 3 and computer_choice == 2:
        print("You win!")
    else:
        print("You lose!")

rock_paper_scissors()
