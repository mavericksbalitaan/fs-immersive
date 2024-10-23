# Gambling game. Create a Boxer class that has size, strength, wins and losses properties. Make sure to use the CONSTRUCTOR function to give values to all these properties.

# In the class create a function that displays the boxer’s stats (Size, Strength, Wins, Losses).

# Create 2 Boxer objects and print out all the information on both boxers.

# Then use the input function to prompt the user to choose which boxer they would like to bet on.

# If the user chooses the boxer that has the best properties in size strength and wins and losses then the user wins their bet. Other wise the user loses.

class Boxer:
    def __init__(self, size, strength, wins, losses):
        self.size = size
        self.strength = strength
        self.wins = wins
        self.losses = losses

    def display_stats(self):
        print(f"Size: {self.size}\nStrength: {self.strength}\nWins: {self.wins}\nLosses: {self.losses}")

boxer1 = Boxer("Large", "Strong", 10, 2)
boxer2 = Boxer("Medium", "Weak", 3, 5)

def game():
    guess = input("Which boxer would you like to bet on? 1 or 2: ")

    if guess == "1":
        if boxer1.size == "Large" and boxer1.strength == "Strong" and boxer1.wins > boxer2.wins and boxer1.losses < boxer2.losses:
            print("You win!")
        else:
            print("You lose!")
    elif guess == "2":
        if boxer2.size == "Large" and boxer2.strength == "Strong" and boxer2.wins > boxer1.wins and boxer2.losses < boxer1.losses:
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid input")

game()

