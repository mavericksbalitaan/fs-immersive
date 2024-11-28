/*
Javascript assignment 1

Print "Hello World" to the console

Print your name and your favorite color to the console

Print the sum of two numbers to the console (Ex: 2+2 = 4)

Use string concatenation to combine your first and last name. Print this to the console.

Create a for loop that prints all values from 1-10

Create a for loop that prints the word "Skillspire" 5 times

Create a for loop that multiplies all values from 1-10 by 2 and print these values out to the console. The output should look like: 2 4 6 8 10 12 14 16 18 20

Create a for loop that prints all EVEN values from 1-20

Create a for loop that prints all ODD values from 1-20

Create a for loop that starts at 1 and ends at 10. If a value is even have the console print out “FIZZ”. If the value is odd have the console print out “BUZZ”.
*/

console.log("Hello World");

console.log("Name: John Doe", "Color: blue");

console.log(2 + 2);

console.log("John" + " " + "Doe");

for (let i = 1; i < 11; i++) {
  console.log(i);
}

for (let i = 1; i < 6; i++) {
  console.log("Skillspire");
}

for (let i = 1; i < 11; i++) {
  console.log(i * 2);
}

for (let i = 1; i < 21; i++) {
  if (i % 2 === 0) {
    console.log(i);
  }
}

for (let i = 1; i < 21; i++) {
  if (i % 2 !== 0) {
    console.log(i);
  }
}

for (let i = 1; i < 10; i++) {
  if (i % 2 === 0) {
    console.log("FIZZ");
  } else {
    console.log("BUZZ");
  }
}
