#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];
const fileError = `Usage: ${process.argv[1]} <filepath>`;
const fileContentError = `Usage: ${process.argv[1]} <filepath> <file content>`;

if (!filePath) {
  console.error(fileError);
  process.exit(1);
}

if (!fileContent) {
  console.error(fileContentError);
  process.exit(1);
}

fs.writeFile(filePath, fileContent, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('File written succesfully...');
  }
});
