# Create a car class that has a top speed property and a function that prints out that top speed property.

# Use this class to write a program that creates a car object and prints out its topspeed.

 # Using the class that you created in the last task create a location property that starts at 0. Then create a drive() function that increases the location variable by 10 miles. Create a stop() function that prints out you’re final location.

class Car:
    def __init__(self, top_speed):
        self.top_speed = top_speed
        self.location = 0

    def print_top_speed(self):
        print(f"The top speed of this car is {self.top_speed} km/h")

    def drive(self):
        self.location += 10

    def stop(self):
        print(f"The final location of the car is {self.location} miles")

car1 = Car(200)
car1.print_top_speed()
car1.drive()
car1.drive()
car1.drive()
car1.stop()

