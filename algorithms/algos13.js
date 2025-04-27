/*
Array Shuffle: Create a function called shuffle(arr), to efficiently shuffle a given array’s values in random order. Hint: Remember the swap method? Use a random number generator to come up index that needs to be swapped. [1,2,3] => [2,1,3], [3,1,2]​
*/

function shuffle(arr) {
  for (let i = 0; i < arr.length; i++) {
    let randindex = Math.floor(Math.random() * (arr.length))
    let temp = arr[i];
    arr[i] = arr[randindex];
    arr[randindex] = temp;
  }
  return arr;
}

console.log(shuffle([1, 2, 3]))

/*
Array: Filter Range. Given arr and values min and max, retain only the array values between min and max indexes. Given [1,2,3,4,5],2,4 return [3,4,5].No built-in array functions. This does not have to be done in place meaning you don't have to return the same array that was passed in as a parameter
*/

function minmax(arr, min, max) {
  let output = []

  for (let i = min; i <= max; i++) {
    output.push(arr[i])
  }
  return output
}

console.log(minmax([1, 2, 3, 4, 5], 2, 4))
