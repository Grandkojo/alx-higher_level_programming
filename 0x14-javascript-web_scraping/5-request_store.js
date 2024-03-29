#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const reqPage = process.argv[2];
const filePath = process.argv[3];

request(reqPage, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  } else {
    const store = body;
    fs.writeFile(filePath, store, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
