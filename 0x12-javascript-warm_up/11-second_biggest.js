#!/usr/bin/node
let r = 0;
const numbers = process.argv.slice(2);
if (process.argv.length >= 3) {
  numbers.sort();
  r = numbers[numbers.length - 2];
}
console.log(r);
