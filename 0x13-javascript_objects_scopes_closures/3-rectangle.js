#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log('x'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
