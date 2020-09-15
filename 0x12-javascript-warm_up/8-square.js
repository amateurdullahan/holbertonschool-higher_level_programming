#!/usr/bin/node

const size = process.argv[2];
if (!Number(size)) {
  console.log('Missing size');
} else {
  for (let c = 0; c < size; c++) {
    for (let d = 0; d < size; d++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
