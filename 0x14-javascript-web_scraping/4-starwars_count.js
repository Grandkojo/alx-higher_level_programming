#!/usr/bin/node

const request = require('request');
const requestmovie = process.argv[2];

if (!requestmovie) {
  console.log(`${process.argv[1]} <movieId>`);
  process.exit(1);
}

request(requestmovie, { json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = body;
    let count = 0;
    films.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
