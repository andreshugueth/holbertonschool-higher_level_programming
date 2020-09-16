#!/usr/bin/node
// Script that prints a square
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing number of occurrences');
} else {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      console.log('X'.repeat(size));
    }
  }
}
