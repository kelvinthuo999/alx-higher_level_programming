#!/usr/bin/node

// Function to execute a given function x times
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the function
module.exports.callMeMoby = callMeMoby;
