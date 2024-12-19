/*
 * Create a function that accepts a string and returns that string but reversed. Example: Given "string"  return "gnirts"​
 */

function reversedString(string) {
  let str = "";
  for (let i = string.length - 1; i >= 0; i--) {
    str += string[i];
  }
  return str;
}

console.log(reversedString("string"));

/*
 * Given an string create a function that checks to see if a string is a palindrome. A palindrome is a word that is spelled the same forward and backwards like “racecar”, “mom”, and “dad”.Hint: Reference the reverse string algorithm.
 */

function palindrome(string) {
  return reversedString(string) == string;
}

console.log(palindrome("racecar"));
