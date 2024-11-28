/*
Javascript Assignment 9


Create a function that accepts an array and replaces all negative values in the array with the word "Negative". Example [-1,2,-3,4,-5] returns ["Negative",2,"Negative",4,"Negative"]

Create a function that accepts a string and returns that string but reversed. Example: Given "string"  return "gnirts"
 */

function replaceNegatives(arr) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      arr[i] = "Negative";
    }
  }
  return arr;
}

console.log(replaceNegatives([-1, 2, -3, 4, -5]));

function reverseString(str) {
  let reversed = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  return reversed;
}

console.log(reverseString("string"));
