// Gambling game. Create a Boxer class that has size, strength, wins and losses properties. Make sure to use the CONSTRUCTOR function to give values to all these properties.

// In the class create a function that displays the boxer’s stats (Size, Strength, Wins, Losses).

// Create 2 Boxer objects and print out all the information on both boxers.

// Then use the input function to prompt the user to choose which boxer they would like to bet on.

// If the user chooses the boxer that has the best properties in size strength and wins and losses then the user wins their bet. Other wise the user loses.

class Boxer {
  constructor(size, strength, wins, losses) {
    this.size = size
    this.strength = strength
    this.wins = wins
    this.losses = losses
  }

  display_stats() {
    console.log(`Size: ${this.size}\nStrength: ${this.strength}\nWins: ${this.wins}\nLosses: ${this.losses}`)
  }
}

let boxer1 = new Boxer("Large", "Strong", 10, 2);
let boxer2 = new Boxer("Medium", "Weak", 3, 5);

function game() {
  let guess = prompt("Which boxer would you like to bet on? 1 or 2: ")

  if (guess == "1") {
    if (boxer1.size == "Large" && boxer1.strength == "Strong" && boxer1.wins > boxer2.wins && boxer1.losses < boxer2.losses) {
      console.log("You win!")
    } else {
      console.log("You lose!")
    }
  } else if (guess == "2") {
    if (boxer2.size == "Large" && boxer2.strength == "Strong" && boxer2.wins > boxer1.wins && boxer2.losses < boxer1.losses) {
      console.log("You win!")
    }
    else {
      console.log("You lose!")
    }
  } else {
    console.log("Invalid input")
  }
}

game()

