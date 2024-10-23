'''
Person and Employee:

- Create a Person class.
- The constructor for the Person class should accept a name and id number as parameters
- In the Person class create a function that displays the persons name and Id number
- Create an Employee class that inherits from the Person class
- The constructor for the Employee class should accept a name, id number, salary and post as parameters
- Inside the constructor use the super function to invoke the constructor of the parent class
- Outside of the Employee class create a new Person object and a new Employee object and pass in the values for both
- Use the display method to print out the information on both employee and person

'''
class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print(f"Name: {self.name}\nID: {self.id}")

class Employee(Person):
    def __init__(self,name,id,salary,post):
        super().__init__(name,id)
        self.salary = salary
        self.post = post
    def display(self):
        super().display()
        print(f"Salary: {self.salary}\nPost: {self.post}")

person1 = Person("John", 123)
person1.display()

employee1 = Employee("Jane", 456, 50000, "Manager")
employee1.display()


