#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let a = 0; a < this.height; a++) {
        for (let b = 0; b < this.width; b++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  }
};
