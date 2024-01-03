#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const requestStarwars = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.log(`${process.argv[1]} <movieId>`);
}

request(requestStarwars, { json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(body.title);
  }
});
