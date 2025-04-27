/*
 * Given a string of words (sentence) create a function that capitalizes every word in the string. Given “hello there skillspire” return “Hello There Skillspire”.
 */

function capitalizeString(string) {
  // solution 1
  // let capitalizeString = "";
  // const splitString = string.split(" ")
  //
  // for (let i = 0; i < splitString.length; i++) {
  //   const newString = splitString[i][0].toUpperCase() + splitString[i].slice(1)
  //   capitalizeString += newString + " "
  // }
  // return capitalizeString

  // solution 2
  let output = string[0].toUpperCase();

  for (let i = 1; i < string.length; i++) {
    output += string[i - 1] == " " ? `${string[i].toUpperCase()}` : string[i]
  }
  return output
}

console.log(capitalizeString("hello there skillspire"));
