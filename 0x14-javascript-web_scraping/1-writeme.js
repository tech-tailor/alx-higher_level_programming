#!/usr/bin/node
// Read and print a file

const fs = require('fs');

// get the file path
const filePath = process.argv[2];
const strToWrite = process.argv[3];

// Read file content
fs.writeFile(filePath, strToWrite, 'utf-8', (err) => {
  if (err) {
    console.error('Error:', err);
  }
});
