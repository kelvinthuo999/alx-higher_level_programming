#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers
    if (w > 0 && h > 0) {
      // Initialize instance attributes width and height
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if conditions are not met
      this.width = undefined;
      this.height = undefined;
    }
  }
}

// Export the Rectangle class
module.exports = Rectangle;
