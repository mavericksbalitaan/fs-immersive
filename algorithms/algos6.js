/*
Count Non-Spaces. Create a function that  accepts a string and returns the number of non-space characters found in the string. For example, given ”lol cool dude", return 11 (not 13).
*/

function countNonspaces(string) {
  let count = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] != " ") {
      count++;
    }
  }
  return count;
}

console.log(countNonspaces("lol cool dude"));
