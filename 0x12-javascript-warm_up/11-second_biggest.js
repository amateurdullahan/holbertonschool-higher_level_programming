#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const a = process.argv.sort(function (a, b) { return b - a; });
  console.log(a[3]);
}
