#!/usr/bin/node

const firstNum = process.argv[2];

if (!isNaN(process.argv[2])) {
  function factorial (num) {
    if (num === 0) {
      return 1;
    } else {
      return num * factorial(num - 1);
    }
  }
  console.log(factorial(Number(firstNum)));
} else {
  console.log(1);
}