#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const key in dict) {
  const nKey = dict[key];
  if (nKey in newDict) {
    newDict[nKey].push(key);
  } else {
    newDict[nKey] = [key];
  }
}
console.log(newDict);
