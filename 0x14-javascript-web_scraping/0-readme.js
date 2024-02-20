#!/usr/bin/node
// Read and print a file

const fs = require('fs');

// get the file path
const filePath = process.argv[2];

// Read file content
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log(data);
  }
});
