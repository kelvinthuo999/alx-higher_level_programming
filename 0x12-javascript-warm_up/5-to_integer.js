#!/usr/bin/node

// Get the first argument passed to the script
const firstArgument = process.argv[2];

// Convert the first argument to an integer
const parsedNumber = parseInt(firstArgument);

// Use console.log(...) to print the output based on the conversion
if (!isNaN(parsedNumber)) {
  console.log(`My number: ${parsedNumber}`);
} else {
  console.log('Not a number');
}
