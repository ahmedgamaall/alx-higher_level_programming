#!/usr/bin/node
// a script that prints the number of
// movies where the character “Wedge Antilles” is present
const getRequest = require('request');
const restApi = process.argv[2];
if (!restApi) process.exit();
getRequest.get(restApi, (error, response, body) => {
  if (!error) {
    const counter = body.split('/people/18/').length - 1;
    console.log(counter);
  }
});
