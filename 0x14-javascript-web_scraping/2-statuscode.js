#!/usr/bin/node
// Read and print a file

const request = require('request');

// get the file path
const url = process.argv[2];

// Read file content
request(
  {
    method: 'GET',
    uri: url,
    encoding: 'utf-8'
  },
  (error, response) => {
    if (error) {
      console.log(error);
    } else {
      console.log('code:', response.statusCode);
    }
  });
