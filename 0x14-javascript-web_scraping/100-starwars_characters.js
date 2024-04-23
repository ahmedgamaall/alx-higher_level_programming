#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
const getRequest = require('request');
const movieId = process.argv[2];
if (!movieId) process.exit();

const restApi = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

getRequest.get(restApi, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const charactersInMovie = JSON.parse(body).characters;
    for (const char of charactersInMovie) {
      getRequest.get(char, (error, response, body) => {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
