#!/usr/bin/node

const argument = process.argv[2];
const number = parseInt(argument);
const x = 'x';

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log(x.repeat(number));
  }
}