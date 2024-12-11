function countOnes(string) {
  let count = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] == 1) {
      count += 1;
    }
  }
  return count;
}

console.log("countOnes:", countOnes("1001011"));

function replaceOnes(string) {
  let newString = "";
  for (let i = 0; i < string.length; i++) {
    if (string[i] == 1) {
      newString += "2";
    } else {
      newString += string[i];
    }
  }
  return newString;
}

console.log("replaceOnes:", replaceOnes("1001011"));
