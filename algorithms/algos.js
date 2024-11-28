/*
https://leetcode.com/problemset/
1.Create a program that prints out all numbers from 10 to 1 in descending order. (This does not have to be in a function)

2.Create a program that prints out all EVEN numbers from 10-1in descending order. HINT: Use modulus operator or have your for loop decrement by 2 (This does not have to be in a function)

3.Create a function that accepts 2 numbers as parameters. Return the larger of the two numbers. For example if given 9 and 10 your function should return 10

4.Create a function that accepts 2 parameters x and y. This function should print out the product of both numbers (x * y), the quotient of both numbers (x/y), the sum of both numbers (x + y), and the difference of both numbers (x-y).
*/

for (let i = 10; i >= 1; i--) {
  console.log(i);
}

for (let i = 10; i >= 1; i--) {
  if (i % 2 === 0) {
    console.log(i);
  }
}

function largerNumber(x, y) {
  if (x > y) {
    return x;
  } else {
    return y;
  }
}

function mathOperations(x, y) {
  console.log(x * y);
  console.log(x / y);
  console.log(x + y);
  console.log(x - y);
}
