#!/usr/bin/node

// Check the number of arguments passed to the script
const numArguments = process.argv.length - 2;

// Use console.log(...) to print the message based on the number of arguments
if (numArguments === 0) {
  console.log('No argument');
} else if (numArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
