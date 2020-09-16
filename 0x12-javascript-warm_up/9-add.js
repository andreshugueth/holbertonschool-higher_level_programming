#!/usr/bin/node
// Script that prints the addition of 2 integers
function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  if (isNaN(num1) || isNaN(num2)) {
    return NaN;
  } else {
    return num1 + num2;
  }
}
console.log(add(process.argv[2], process.argv[3]));
