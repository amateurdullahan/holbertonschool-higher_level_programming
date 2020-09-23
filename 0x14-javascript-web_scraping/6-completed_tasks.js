#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  const result = {};
  for (const obj in json) {
    if (json[obj].completed) {
      if (result[json[obj].userId]) {
        result[json[obj].userId] += 1;
      } else {
        result[json[obj].userId] = 1;
      }
    }
  }
  console.log(result);
});
