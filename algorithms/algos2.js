/*
Create a program that calculates the product off all of the numbers from 1 to 5 (12345). The final product for this program should be 120. (This does not have to be a function). Hint: Use a for loop that starts from 1 to 5. Where are you going to save the product? ​
 */

let product = 1;

for (let i = 1; i <= 5; i++) {
  product *= i;
}

console.log(product);

/*
Find the Average: Create a function that accepts an array as a parameter and calculates the sum of all the numbers in the array. Afterwards return that sum divided by the number of values in the array. Given [1,2,3,4,5], return 3. Hint: Use a for loop that starts from 0 to array.length. Where are you going to save the sum?
  */

function avg(array) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }

  return sum / array.length;
}

console.log(avg([1, 2, 3, 4, 5]));
