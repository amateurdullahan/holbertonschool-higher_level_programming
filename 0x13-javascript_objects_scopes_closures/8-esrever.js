#!/usr/bin/node

exports.esrever = function (list) {
  let nList = [];
  for (let c = list.length - 1; c >= 0; c--) {
    nList.push(list[c]);
  }
  return nList;
}
