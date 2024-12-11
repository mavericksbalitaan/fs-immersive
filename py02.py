import random

# Parent Class / Base Class
class BigCat:
    def __init__(self, speed=5, strength=5, intelligence=5, health=5, durability=5):
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.health = health
        self.durability = durability


# Child Class / Derived Class
# Parent: BigCat
# Child: Lion
class Lion(BigCat):
    def __init__(self, speed=5, strength=50, intelligence=5, health=50, durability=5):
        # self.speed = speed
        # self.strength = strength
        # self.intelligence = intelligence
        # self.health = health
        # self.durability = durability
        super().__init__(speed, strength, intelligence, health, durability)

    def king(self, bigcat):
        if isinstance(bigcat, Cheetah) == True:
            # if type(bigcat) == Cheetah:
            myrandom = random.random()
            print(f"myrandom: {myrandom}")
            if myrandom > 0.6:
                pass
            else:
                bigcat.speed = 0
                bigcat.strength = 0
                bigcat.intelligence = 0
                bigcat.health = 0
                bigcat.durability = 0
        else:
            bigcat.speed = 0
            bigcat.strength = 0
            bigcat.intelligence = 0
            bigcat.health = 0
            bigcat.durability = 0


# Parent: BigCat
# Child: Cheetah
class Cheetah(BigCat):
    def __init__(
        self, speed=75, strength=25, intelligence=25, health=25, durability=25
    ):
        super().__init__(speed, strength, intelligence, health, durability)


bigcat1 = BigCat()
lion1 = Lion()
cheetah1 = Cheetah()

def game():
    lion1.king(cheetah1)
    print("lion1:", lion1.speed)
    print("cheetah1:", cheetah1.speed)
    lion1.king(cheetah1)
    print("cheetah1:", cheetah1.speed)


game()

# lion1.king(bigcat1)
# print("bigcat1:", bigcat1.speed)
# print("bigcat1:", bigcat1.health)
# print("bigcat1:", bigcat1.durability)

# # This is class Person
# class Person:
#     # this is the constructor method
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def display(self):
#         print(f"Name: {self.name} ID: {self.id}")
#
#
# # This is class Employee
# class Employee(Person):
#     def __init__(self, name, id, salary, post):
#         super().__init__(name, id)
#         self.salary = salary
#         self.post = post
#     def display(self):
#         print(f"Name: {self.name} ID: {self.id} Salary: {self.salary} Post: {self.post}")
#
#
# person1 = Person("Jane", 1)
# person1.display()
#
# print(type(person1))
#
# employee1 = Employee("Alex", 202, 1000, "Manager")
# employee1.display()
#
# print(type(employee1))
#
# print(isinstance(person1, Employee))


# class Boxer:
#     def __init__(self, name, size, strength, wins, losses):
#         self.name = name
#         self.size = size
#         self.strength = strength
#         self.wins = wins
#         self.losses = losses
#     def displayStats(self):
#         print(f"Name: {self.name} Size: {self.size} Strength: {self.strength} Wins: {self.wins} Losses: {self.losses}")
#
# boxer1 = Boxer("Jake", "Small", 5, 20, 10)
# boxer2 = Boxer("Tyson", "Medium", 7, 25, 5)
#
# boxer1.displayStats()
# boxer2.displayStats()
#
#
#
# def gamblingGame():
#     user_choice = int(input("Choose 1 for boxer1 and type 2 for boxer2:"))
#
#     if user_choice == 1 and (boxer1.wins/boxer1.losses) > (boxer2.wins/boxer2.losses):
#         print(f"You win")
#     elif user_choice == 1 and (boxer1.wins/boxer1.losses) < (boxer2.wins/boxer2.losses):
#         print(f"You lose")
#     elif user_choice ==2 and (boxer1.wins/boxer1.losses) > (boxer2.wins/boxer2.losses):
#         print(f"You lose")
#     else:
#         print(f"You win")
#
# gamblingGame()
