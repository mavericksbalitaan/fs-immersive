'''
Question 1: Temperature Conversion Program
Use the input function to prompt the user for the current temperature in their area in Fahrenheit.  This program should convert and print the temperature given from Fahrenheit to both Celsius using the conversion formula below.

The formulas for conversion are:

Celsius: (Fahrenheit - 32) * 5/9
'''

def temp_conversion():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"The temperature in Celsius is {celsius}")

temp_conversion()

'''
Question 2: Generate Random Number
Create a function generate_random_numbers(start, end) that generates a random number between start and end (inclusive) and returns it.
Use the random.randint() function from the random module to generate the random number.
'''

import random

def generate_random_numbers(start, end):
    return random.randint(start, end)

print(generate_random_numbers(1, 10))

'''
Question 3: OOP game
Create a base Human class with five attributes: name, strength, intelligence, dexterity, and health.
Give a default value of 3 for strength, intelligence, and dexterity. Health should have a default of 100.
When an object is constructed from this class it should have the ability to pass a name
Now add a new method called attack, which when invoked, should attack another Human object that is passed as a parameter. The damage done should be 5 * strength (5 points of damage to the attacked, for each 1 point of strength of the attacker).
Create a class for a Ninja, a Wizard, and a Samurai (All of them should inherit from the human class)
Wizard should have a default health of 50 and intelligence of 25
Wizard should have a method called heal, which when invoked, heals the Wizard by 10 * intelligence
Wizard should have a method called fireball, which when invoked, decreases the health of whichever object it attacked by some random integer between 20 and 50
Ninja should have a default dexterity of 175
Ninja should have a steal method, which when invoked, attacks an object and increases the Ninjas health by 10
Ninja should have a get_away method, which when invoked, decreases its health by 15
Samurai should have a default health of 200
Samurai should have a method called death_blow, which when invoked should attack an object and decreases its health to 0 if it has less than 50 health
Samurai should have a method called meditate, which when invoked, heals the Samurai back to full health
'''

class Human:
    def __init__(self, name, strength=3, intelligence=3, dexterity=3, health=100):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.health = health

    def attack(self, target):
        target.health -= 5 * self.strength
        print(f"{self.name} attacked {target.name} for {5 * self.strength} damage")

class Wizard(Human):
    def __init__(self, name, strength=3, intelligence=25, dexterity=3, health=50):
        super().__init__(name, strength, intelligence, dexterity, health)

    def heal(self):
        self.health += 10 * self.intelligence
        print(f"{self.name} healed for {10 * self.intelligence}")

    def fireball(self, target):
        target.health -= random.randint(20, 50)
        print(f"{self.name} attacked {target.name} with a fireball")

class Ninja(Human):
    def __init__(self, name, strength=3, intelligence=3, dexterity=175, health=100):
        super().__init__(name, strength, intelligence, dexterity, health)

    def steal(self, target):
        target.health -= 10
        self.health += 10
        print(f"{self.name} stole from {target.name}")

    def get_away(self):
        self.health -= 15
        print(f"{self.name} got away")

class Samurai(Human):
    def __init__(self, name, strength=3, intelligence=3, dexterity=3, health=200):
        super().__init__(name, strength, intelligence, dexterity, health)

    def death_blow(self, target):
        if target.health < 50:
            target.health = 0
            print(f"{self.name} dealt a death blow to {target.name}")
        else:
            print(f"{self.name} failed to deal a death blow to {target.name}")

    def meditate(self):
        self.health = 200
        print(f"{self.name} meditated")

human1 = Human("John")
human2 = Human("Jane")
human1.attack(human2)
print(human2.health)

wizard1 = Wizard("Wizard")
wizard2 = Wizard("Wizard2")
wizard1.heal()
wizard1.fireball(wizard2)
print(wizard2.health)

ninja1 = Ninja("Ninja")
ninja2 = Ninja("Ninja2")
ninja1.steal(ninja2)
print(ninja1.health)
ninja1.get_away()
print(ninja1.health)

samurai1 = Samurai("Samurai")
samurai2 = Samurai("Samurai2")
samurai1.death_blow(samurai2)
print(samurai2.health)
samurai2.health = 40
samurai1.death_blow(samurai2)
print(samurai2.health)
samurai1.meditate()
print(samurai1.health)

