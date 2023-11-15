#!/usr/bin/node

// Get the first argument passed to the script
const firstArgument = process.argv[2];

// Use console.log(...) to print the output based on the presence of the first argument
if (firstArgument === undefined) {
  console.log('No argument');
} else {
  console.log(firstArgument);
}
