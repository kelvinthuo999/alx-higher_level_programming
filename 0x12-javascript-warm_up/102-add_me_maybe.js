#!/usr/bin/node

// Function to increment a number and call another function
function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}

// Export the function
module.exports.addMeMaybe = addMeMaybe;
