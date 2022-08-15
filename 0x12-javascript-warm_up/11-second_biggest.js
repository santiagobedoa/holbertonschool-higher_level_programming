#!/usr/bin/node
let r = 0;
const numbers = process.argv.slice(2);
if (numbers.length > 1) {
  numbers.sort((a, b) => a - b);
  r = numbers[numbers.length - 2];
}
console.log(r);
