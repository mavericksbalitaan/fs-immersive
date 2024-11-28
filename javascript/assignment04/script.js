/*
Javascript Assignment 4

Create a console based assignment that prompts the user for their:

Full Name
Favorite Food
Favorite Activity



After the user has submitted their data.
Write the information to the HTML document
All of the data should display as <h1> tags .
All the console based program should be written inside of a function
*/

function userInformation() {
  var fullname = prompt("What is your full name?");
  var favFood = prompt("What is your favorite food?");
  var favActivity = prompt("What is your favorite activity?");

  document.write(`<h1>${fullname}</h1>`);
  document.write(`<h1>${favFood}</h1>`);
  document.write(`<h1>${favActivity}</h1>`);
}

userInformation();
