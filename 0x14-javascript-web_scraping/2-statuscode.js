#!/usr/bin/node
// a script that display the status code of a GET request
const getRequest = require('request');

getRequest.get(process.argv[2], (error, response, body) => {
  if (!error) console.log('code:', response.statusCode);
});
