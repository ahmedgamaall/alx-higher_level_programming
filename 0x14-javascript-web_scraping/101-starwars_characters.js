#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];
if (!movieId) process.exit();

const restApi = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function makeRequest (url, charactersInMovie, index) {
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < charactersInMovie.length) {
        makeRequest(charactersInMovie[index + 1], charactersInMovie, index + 1);
      }
    }
  });
}

request.get(restApi, (error, response, body) => {
  if (!error) {
    const charactersInMovie = JSON.parse(body).characters;
    makeRequest(charactersInMovie[0], charactersInMovie, 0);
  } else console.log(error);
});
