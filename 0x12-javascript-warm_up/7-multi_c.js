#!/usr/bin/node

const argument = process.argv[2];
const number = parseInt(argument);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}