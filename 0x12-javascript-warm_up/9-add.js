#!/usr/bin/node
// Script that prints the addition of 2 integers
function add (a, b) {
  const num_1 = parseInt(a);
  const num_2 = parseInt(b);
  if (isNaN(num_1) || isNaN(num_2)) {
    return NaN;
  } else {
    return num_1 + num_2;
  }
}
console.log(add(process.argv[2], process.argv[3]));
