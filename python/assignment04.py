# Create a python guessing game using the input() function. The program should create a number variable that ranges from 1-10. Then use the input() function to have the user guess the number. If the number is too big print to the user “The number is too big guess again”, If the number is too small print to the user “The number is too small guess again”. If the number is the correct number then print to the user that they guessed successfully.

def guessing_game():
    import random
    number = random.randint(1,10)
    guess = int(input("Guess a number between 1-10: "))
    while guess != number:
        if guess > number:
            print("The number is too big guess again")
            guess = int(input("Guess a number between 1-10: "))
        else:
            print("The number is too small guess again")
            guess = int(input("Guess a number between 1-10: "))
    print("You guessed successfully")

guessing_game()

