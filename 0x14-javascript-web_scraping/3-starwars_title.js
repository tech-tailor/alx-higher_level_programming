#!/usr/bin/node
// Read and print a file

const request = require('request');

// get the file path
const movieID = process.argv[2];
const baseURL = 'https://swapi-api.alx-tools.com/api/films/';
const url = baseURL + movieID;

// Read file content
request(
  {
    method: 'GET',
    uri: url,
    encoding: 'utf-8'
  },
  (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      // parse the string to JSON
      const parsedBody = JSON.parse(body);
      console.log(parsedBody.title);
    }
  });
