#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 0 || h < 0 || w === undefined || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let c = 0; c < this.height; c++) {
      for (let d = 0; d < this.width; d++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
};
