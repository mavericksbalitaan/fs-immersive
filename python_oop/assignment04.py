"""
King of the Jungle:

Assignment Hint: https://www.geeksforgeeks.org/type-isinstance-python/Links to an external site.

- Create a Big Cat class
- Give the class properties of speed, strength, intelligence, health and durability. And set all attributes to 5
- Create a Lion class that inherits from the BigCat class and set the Lion's strength to 50 and health to 50
- Give the Lion class a method called king() that accepts a BigCat object as a parameter and depletes all the objects attributes (sets them to 0). If the object is a Cheetah then it should have a 60% chance of leaving unscathed. (Hint use a random number generator)
- Create a Leopard class that inherits from the BigCat class and set the Leopard's strength, intelligence, and health to 30
- Give the Leopard a method called attack that accepts a BigCat object. If the object is a lion then you must run the Lion's king()  function, if the object is anything else then you must deplete the objects health by 15points. If the object is a Cheetah then it should have a 60% chance of leaving unscathed. (Hint use a random number generator)
- Create a Cheetah class that inherits from the BigCat class and set the Cheetah's speed to 75, and the rest of its attributes to 25
- Give the Cheetah a method called run() that accepts a BigCat object. If it encounter's a Leopard run the Leopard's attack method. If it encounters the Lion run the Lion's king() method.
- If the Cheetah runs away from any of its foes then they lose 20 points in health.
- Now after doing all of this try to create a game where ALL objects get created and All their methods are used. In the end there should only be one winner. Challenge: Try to make your game challenging enough so that the Lion doesn't win every single time.

"""

import random


class BigCat:
    def __init__(self, speed=5, strength=5, intelligence=5, health=5, durability=5):
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.health = health
        self.durability = durability

    def printStats(self):
        print(
            f"Type: {type(self)} Speed: {self.speed}, Strength: {self.strength}, Intelligence: {self.intelligence}, Health: {self.health}, Durability: {self.durability}"
        )


class Lion(BigCat):
    def __init__(self, speed=5, strength=50, intelligence=5, health=50, durability=5):
        super().__init__(speed, strength, intelligence, health, durability)

    def king(self, obj):
        if isinstance(obj, Cheetah):
            chance = random.random()
            print(f"Cheetah's survival rate: {round(chance, 2)}")
            if chance > 0.6:
                print("The Cheetah escaped unscathed")
            else:
                obj.speed = 0
                obj.strength = 0
                obj.intelligence = 0
                obj.health = 0
                obj.durability = 0
        else:
            obj.speed = 0
            obj.strength = 0
            obj.intelligence = 0
            obj.health = 0
            obj.durability = 0


class Leopard(BigCat):
    def __init__(self, speed=5, strength=30, intelligence=30, health=30, durability=5):
        super().__init__(speed, strength, intelligence, health, durability)

    def attack(self, obj):
        if isinstance(obj, Lion):
            obj.king(self)
        elif isinstance(obj, Cheetah):
            chance = random.random()
            print(f"Cheetah's survival rate: {round(chance, 2)}")
            if chance > 0.6:
                print("The Cheetah escaped unscathed")
                return
        obj.health -= 15


class Cheetah(BigCat):
    def __init__(self, speed=75, strength=25, intelligence=25, health=25, durability=5):
        super().__init__(speed, strength, intelligence, health, durability)

    def run(self, obj):
        if isinstance(obj, Leopard):
            obj.attack(self)
        elif isinstance(obj, Lion):
            obj.king(self)
        else:
            chance = random.random()
            print(f"Cheetah's survival rate: {round(chance, 2)}")
            if chance > 0.6:
                print("The Cheetah escaped unscathed")
                return
            else:
                obj.health -= 20


#
# cheetah.run(lion)
# cheetah.run(leopard)
#
# print(f"Lion: {lion.__dict__}")
# print(f"Leopard: {leopard.__dict__}")
# print(f"Cheetah: {cheetah.__dict__}")


def game():
    lion = Lion()
    leopard = Leopard()
    cheetah = Cheetah()

    lion.printStats()
    leopard.printStats()
    cheetah.printStats()

    # lion.king(leopard)
    # leopard.printStats()
    #
    # lion.king(cheetah)
    # cheetah.printStats()

    # leopard.attack(cheetah)
    # cheetah.printStats()

    # leopard.attack(lion)
    # leopard.printStats()

    # cheetah.run(lion)
    # cheetah.printStats()

    # cheetah.run(leopard)
    # cheetah.printStats()


game()
