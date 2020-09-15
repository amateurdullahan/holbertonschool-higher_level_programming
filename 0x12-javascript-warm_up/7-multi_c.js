#!/usr/bin/node
const x = process.argv[2]

if (!Number(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let c = 0; c < x; c++) {
    console.log('C is fun');
  }
}
