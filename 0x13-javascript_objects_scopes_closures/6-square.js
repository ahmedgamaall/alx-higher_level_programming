#!/usr/bin/node
const ImportedSquareFive = require('./5-square');

class Square extends ImportedSquareFive {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
