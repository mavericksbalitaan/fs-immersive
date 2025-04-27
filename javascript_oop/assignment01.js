// Create a car class that has a top speed property and a function that prints out that top speed property.

// Use this class to write a program that creates a car object and prints out its topspeed.

// Using the class that you created in the last task create a location property that starts at 0. Then create a drive() function that increases the location variable by 10 miles. Create a stop() function that prints out you’re final location.

class Car {
  constructor(top_speed) {
    this.top_speed = top_speed
    this.location = 0
  }

  print_top_speed() {
    console.log(`The top speed of this car is ${this.top_speed} km/h`)
  }

  drive() {
    this.location += 10
  }

  stop() {
    console.log(`The final location of the car is ${this.location} miles`)

  }
}

let car1 = new Car(200)
car1.print_top_speed()
car1.drive()
car1.drive()
car1.drive()
car1.stop()

