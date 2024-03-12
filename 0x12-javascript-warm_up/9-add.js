#!/usr/bin/node

const firstNum = process.argv[2];
const secondNum = process.argv[3];

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(firstNum, secondNum));