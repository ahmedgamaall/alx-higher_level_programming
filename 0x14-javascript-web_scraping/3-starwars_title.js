#!/usr/bin/node
// a script that prints the title of a Star
// Wars movie where the episode number matches a given integer
const getRequest = require('request');
const movieId = process.argv[2];
if (!movieId) process.exit();

const restApi = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
getRequest.get(restApi, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const move = JSON.parse(body);
    console.log(move.title);
  }
});
