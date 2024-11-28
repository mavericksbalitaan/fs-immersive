/*
Javascript Assignment 3

Using the User Input module as a reference . Create a console based program that prompts the user to input their age.

For users 16 and under print out "Stay home, study, and get your drivers license"

For users that are between 18 and 21 print out "Have some fun, but not TOO much fun. You're still a young adult"

For users 21 and over print out "Have fun. But be responsible. You are in control of your life"

The code for the console based program should be written inside of a function
 */

var age = prompt("Please enter your age: ");

function ageChecker(age) {
  if (age <= 16) {
    console.log("Stay home, study, and get your drivers license");
  } else if (age >= 18 && age <= 21) {
    console.log("Have some fun, but not TOO much fun. You're still a young adult");
  } else {
    console.log("Have fun. But be responsible. You are in control of your life");
  }
}

ageChecker(age);
