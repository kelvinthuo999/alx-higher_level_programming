#!/usr/bin/node

// Get the first argument passed to the script
const argument = process.argv[2];

// Convert the argument to an integer
const size = parseInt(argument);

// Check if the conversion is successful
if (!isNaN(size)) {
  // Loop to print a square of size
  for (let i = 0; i < size; i++) {
    let squareLine = '';
    for (let j = 0; j < size; j++) {
      squareLine += 'X';
    }
    console.log(squareLine);
  }
} else {
  console.log('Missing size');
}
