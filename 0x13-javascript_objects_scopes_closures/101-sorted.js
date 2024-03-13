#!/usr/bin/node
const oDict = require('./101-data').dict;

const totalist = Object.entries(oDict);
const values = Object.values(oDict);
const uniqValues = [...new Set(values)];
const nDict = {};
for (const i in uniqValues) {
  const lt = [];
  for (const j in totalist) {
    if (totalist[j][1] === uniqValues[i]) {
      lt.unshift(totalist[j][0]);
    }
  }
  nDict[uniqValues[i]] = lt;
}
console.log(nDict);
