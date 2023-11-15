#!/usr/bin/node

const input = process.argv[2];

function factorial (n) {
  // Base case: factorial of 0 or 1 is 1
  if (n === 0 || n === 1) {
    return 1;
  }

  // Recursive case: n! = n * (n-1)!
  return n * factorial(n - 1);
}

// Convert the input to an integer and compute the factorial
const parsedInput = parseInt(input);
const result = isNaN(parsedInput) ? 1 : factorial(parsedInput);

// Print the result
console.log(result);
