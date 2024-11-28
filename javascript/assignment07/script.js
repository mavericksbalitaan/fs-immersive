/*
Javascript Assignment


Create a webpage that takes input from the user and writes that data to the DOM:

This data should be collected using a form.

The form should collect the user's first name, last name, email, and age

Use Javascript to print this out to the DOMLinks to an external site.
 */

let form = document.querySelector("form");

form.addEventListener("submit", function(e) {
  e.preventDefault();
  let firstName = document.querySelector("#fname").value;
  let lastName = document.querySelector("#lname").value;
  let email = document.querySelector("#email").value;
  let age = document.querySelector("#age").value;

  document.body.innerHTML += `<h1>First Name: ${firstName}</h1> <br> <h1>Last Name: ${lastName}</h1> <br> <h1>Email: ${email}</h1> <br> <h1>Age: ${age}</h1>`;
});
