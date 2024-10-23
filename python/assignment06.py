'''
Roll the dice.

1. Prompt the user for a value between 1 and 6

2. Emulate a dice rolling session. (Use Random Number Generator)

3. If the user rolls the number that they were prompted for then print "You have successfully rolled (number that they chose)"

4. You must also print out the number of tries that it took the user to roll that number.

'''

def roll_the_dice():
    import random
    user_choice = int(input("Choose a number between 1 and 6: "))
    dice = random.randint(1,6)
    tries = 1
    while dice != user_choice:
        dice = random.randint(1,6)
        tries += 1
    print(f"You have successfully rolled {user_choice} in {tries} tries")

roll_the_dice()
