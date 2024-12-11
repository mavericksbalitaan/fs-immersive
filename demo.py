import random
# Generate a random number between 1-10
computer_guess = random.randint(1, 10)
# Counter for number of user guesses
count = 0
# print(f"Computer guess {computer_guess}")

# First Attempt
def guessing_game():
    user_guess = int(input("Guess a number between 1-10: "))
    count = 0
    # print(user_guess)
    # print(type(user_guess))

    if computer_guess == user_guess:
        count += 1
        print(f"You guessed successfully in {count} tries")
    elif computer_guess > user_guess:
        count += 1
        print("The number is too small guess again")
        guessing_game()
    else:
        print("The number is too big guess again")
        count += 1
        guessing_game()

# guessing_game()

# Second Attempt
# while True:
#     user_guess = int(input("Guess a number between 1-10: "))
#     print(user_guess)
#
#     if computer_guess == user_guess:
#         count += 1
#         print(f"You guessed successfully in {count} tries")
#         break
#     elif computer_guess > user_guess:
#         print("The number is too small guess again")
#         count += 1
#     else:
#         print("The number is too big guess again")
#         count += 1
#
# (1=Rock, 2=Paper, or 3=Scissors)

computer_choice = random.randint(1, 3)
print(f"Computer choice {computer_choice}")

while True:
    user_choice = int(input("Guess a number between 1 to 3: "))
    if user_choice == 1 and computer_choice == 2:
        print("You lose")
    elif user_choice == 1 and computer_choice == 3:
        print("You win")
        break
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
        break
    elif user_choice == 2 and computer_choice == 3:
        print("You lose")
    elif user_choice == 3 and computer_choice == 1:
        print("You lose")
    elif user_choice == 3 and computer_choice == 2:
        print("You win")
        break
    else:
        print("It's a tie")

def rps():
    user_choice = int(input("Guess a number between 1 to 3: "))
    if user_choice == 1 and computer_choice == 2:
        print("You lose")
        rps()
    elif user_choice == 1 and computer_choice == 3:
        print("You win")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    elif user_choice == 2 and computer_choice == 3:
        print("You lose")
        rps()
    elif user_choice == 3 and computer_choice == 1:
        print("You lose")
        rps()
    elif user_choice == 3 and computer_choice == 2:
        print("You win")
    else:
        print("It's a tie")
        rps()

rps()
