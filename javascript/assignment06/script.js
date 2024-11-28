/*
Javascript Assignment 6

Store a link to 3 different images in an Array. Iterate through that array and display all of the images. Here's an example of what it looks like to store a link to an image in an Array:

var arr = ["<img src = 'test.png' alt = 'test image'>"]
 */

var image = "<img src='https://place-hold.it/200x300' alt='placeholder image'>";
var arr = [image, image, image];

for (let i = 0; i < arr.length; i++) {
  document.write(arr[i]);
}

