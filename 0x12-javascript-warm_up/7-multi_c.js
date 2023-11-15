#!/usr/bin/node

// Get the first argument passed to the script
const argument = process.argv[2];

// Convert the argument to an integer
const numOccurrences = parseInt(argument);

// Check if the conversion is successful
if (!isNaN(numOccurrences)) {
  // Loop to print "C is fun" x times
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
