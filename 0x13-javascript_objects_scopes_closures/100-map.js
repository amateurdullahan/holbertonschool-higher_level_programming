#!/usr/bin/node
const data = require('./100-data').list;
const newList = list.map((x, i) => x * i);
console.log(data);
console.log(newList);
