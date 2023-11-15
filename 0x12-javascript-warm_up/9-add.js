#!/usr/bin/node

const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  return a + b;
}

const parsedA = parseInt(a);
const parsedB = parseInt(b);

console.log(add(parsedA, parsedB));
