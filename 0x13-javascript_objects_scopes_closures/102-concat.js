#!/usr/bin/node
const fileDic = require('fs');

const firstArg = fileDic.readFileSync(process.argv[2]).toString();
const secondArg = fileDic.readFileSync(process.argv[3]).toString();
fileDic.writeFileSync(process.argv[4], firstArg + secondArg);
