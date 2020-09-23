#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  let c = 0;
  for (let a = 0; a < json.results.length; a++) {
    for (let b = 0; b < json.results[a].characters.length; b++) {
      if (json.results[a].characters[b === 'https://swapi-api.hbtn.io/api/people/18/']) {
        c += 1;
      }
    }
  }
  console.log(c);
});
