'''
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

'''

import random

class BigCat:
    def __init__(self):
        self.speed = 5
        self.strength = 5
        self.intelligence = 5
        self.health = 5
        self.durability = 5

class Lion(BigCat):
    def __init__(self):
        super().__init__()
        self.strength = 50
        self.health = 50

    def king(self, obj):
        if isinstance(obj, Cheetah):
            chance = random.randint(1, 100)
            if chance <= 60:
                print("The Cheetah escaped unscathed")
                return
        obj.speed = 0
        obj.strength = 0
        obj.intelligence = 0
        obj.health = 0
        obj.durability = 0

class Leopard(BigCat):
    def __init__(self):
        super().__init__()
        self.strength = 30
        self.intelligence = 30
        self.health = 30

    def attack(self, obj):
        if isinstance(obj, Lion):
            obj.king(obj)
        elif isinstance(obj, Cheetah):
            chance = random.randint(1, 100)
            if chance <= 60:
                print("The Cheetah escaped unscathed")
                return
        obj.health -= 15

class Cheetah(BigCat):
    def __init__(self):
        super().__init__()
        self.speed = 75
        self.strength = 25
        self.intelligence = 25
        self.health = 25

    def run(self, obj):
        if isinstance(obj, Leopard):
            obj.attack(obj)
        elif isinstance(obj, Lion):
            obj.king(obj)
        else:
            chance = random.randint(1, 100)
            if chance <= 60:
                print("The Cheetah escaped unscathed")
                obj.health -= 20
                return
            obj.health -= 20

lion = Lion()
leopard = Leopard()
cheetah = Cheetah()

lion.king(leopard)
leopard.attack(cheetah)

cheetah.run(lion)
cheetah.run(leopard)

print(f"Lion: {lion.__dict__}")
print(f"Leopard: {leopard.__dict__}")
print(f"Cheetah: {cheetah.__dict__}")


