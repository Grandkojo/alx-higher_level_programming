#!/usr/bin/node

const requestMod = require('request');
const requestArg = process.argv[2];

requestMod(requestArg, function (error, response, body) {
  if (error) {
    console.error('Error: ', error);
    return;
  }
  return console.log('code:', response.statusCode);
});
