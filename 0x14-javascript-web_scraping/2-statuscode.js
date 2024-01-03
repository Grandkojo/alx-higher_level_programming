#!/usr/bin/node

const requestMod = require('request');
const requestArg = process.argv[2];

requestMod(requestArg, function (err, response, body) {
  if (err) {
    console.error('Error: ', err);
  }
  console.log('code: ', response.statusCode);
});
