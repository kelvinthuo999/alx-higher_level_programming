#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Check if w and h are numbers and positive integers
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      // If conditions are met, initialize width and height
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
