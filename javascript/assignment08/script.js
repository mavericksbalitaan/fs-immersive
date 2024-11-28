/*
Javascript Assignment 8

Create a button that changes the color of a division when clicked.
 */

let btn = document.querySelector("button");
let container = document.querySelector(".container");

container.style.width = "200px";
container.style.height = "200px";
container.style.border = "1px solid black";

btn.addEventListener("click", function() {
  container.style.backgroundColor = "red";
});
