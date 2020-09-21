#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let c = 0; c < list.length; c++) {
    if (list[c] === searchElement) {
      count += 1;
    }
  }
  return count;
};
