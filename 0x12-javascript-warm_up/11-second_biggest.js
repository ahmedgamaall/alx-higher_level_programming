#!/usr/bin/node

const argList = process.argv.slice(2);
const nums = argList.map(argument => parseInt(argument));

if (nums.length < 2) {
  console.log(0);
} else {
  const sortedNums = nums.sort((a, b) => b - a);
  console.log(sortedNums);
}