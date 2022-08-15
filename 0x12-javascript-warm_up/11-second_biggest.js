#!/usr/bin/node
const numbers = process.argv.slice(2);
let r = 0;
if (numbers.length > 1) {
  numbers.sort();
  r = numbers[numbers.length - 2];
}
console.log(r);
