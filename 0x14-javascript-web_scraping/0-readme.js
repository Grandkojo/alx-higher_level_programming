#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const fileError = `Usage: ${process.argv[1]} <filename>`;

if (!filePath) {
  console.error(fileError);
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  return console.log(data);
});
