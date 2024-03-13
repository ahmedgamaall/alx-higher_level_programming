#!/usr/bin/node
const lt = require('./100-data.js').list;
console.log(lt);
console.log(lt.map((e, i) => e * i));
