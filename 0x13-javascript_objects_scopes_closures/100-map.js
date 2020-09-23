#!/usr/bin/node
const data = require('./100-data').list;
const newList = list.map((num, index) => num * index);
console.log(data);
console.log(newList);
