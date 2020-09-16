#!/usr/bin/node
// script that computes and prints a factorial
function factorial (a) {
  let val = 1;
  for (let i = 1; i <= a; i++) {
    val *= i;
  }
  return val;
}
console.log(factorial(process.argv[2]));
