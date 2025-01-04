/*
Given an array, move all values forward (to the left) by one index dropping the first value and leaving a 0 (zero) value at the end of the array.
Given [1,2,3,4,5] return [2,3,4,5,0]
  */

function shiftArrayValues(array) {
  for (let i = 0; i < array.length; i++) {
    array[i] = array[i + 1];
  }
  array[array.length - 1] = 0;
  return array;
}

console.log(shiftArrayValues([1, 2, 3, 4, 5]));

/*
Given an array with only 2 values. Swap the places of those 2 values and return the altered array. Given [1,2] return [2,1]​
 */

function swapValues(array) {
  let temp = array[0];
  array[0] = array[1];
  array[1] = temp;

  return array;
}

console.log(swapValues([1, 2]));

/*
Array swap pairs. Swap positions of successive pairs of values of a given array. If length is odd, do not change the final element. For [1,2,3,4], return [2,1,4,3]. For example, change input ["Brendan",true,42] to [true,"Brendan",42]. As with all array challenges, do this without using any built-in array methods.
 */

function swapPairs(array) {
  for (let i = 0; i < array.length; i += 2) {
    let temp = array[i];
    array[i] = array[i + 1];
    array[i + 1] = temp;
  }
  return array;
}

console.log(swapPairs([1, 2, 3, 4]));
