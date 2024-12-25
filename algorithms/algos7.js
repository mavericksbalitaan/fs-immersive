/*
  Create a function that accepts a list and a parameter N return the element that is N-from-array’s-end.
  Given ([5,2,3,6,4,9,7],3) , return 4. If the array is too short, return null .
*/

function returnNfromArrayEnd(array, N) {
  return array[array.length - N];
}

console.log(returnNfromArrayEnd([5, 2, 3, 6, 4, 9, 7], 3));

/*
  Create a function that accepts an array of numbers and a number Y as a parameters.
  Return a count of all of the numbers that are greater than Y. Example (Given [1,2,3,4,5] and y=2 return 3.
  In this case 2 will be our Y)
*/

function greaterThanY(array, Y) {
  let count = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] > Y) {
      count++;
    }
  }
  return count;
}

console.log(greaterThanY([1, 2, 3, 4, 5], 2));
