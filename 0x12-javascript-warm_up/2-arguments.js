#!/usr/bin/node
const countargs = process.argv.length;
if (countargs === 2) {
  console.log('No argument');
} else if (countargs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
