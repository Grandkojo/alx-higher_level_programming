#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let c = 0; c < x; c++) row += 'X';
    console.log(row);
  }
}
