#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file
const fileds = require('fs');
const getRequest = require('request');

if (process.argv.length > 3) {
  getRequest.get(process.argv[2], (error, resopnse, body) => {
    if (error) console.log(error);
    else {
      fileds.writeFile(process.argv[3], body, 'utf8', (error) => {
        if (error) console.log(error);
      });
    }
  });
}
