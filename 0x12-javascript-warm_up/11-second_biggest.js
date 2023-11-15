#!/usr/bin/node

const args = process.argv.slice(2);

function findSecondLargest (numbers) {
  // If no arguments passed, print 0
  if (numbers.length === 0) {
    return 0;
  }

  // If only one argument passed, print 0
  if (numbers.length === 1) {
    return 0;
  }

  // Convert arguments to integers
  const integers = numbers.map(Number);

  // Sort the array in descending order
  const sortedIntegers = integers.sort((a, b) => b - a);

  // Find the second largest integer
  const secondLargest = sortedIntegers[1];

  return secondLargest;
}

// Print the result
console.log(findSecondLargest(args));
