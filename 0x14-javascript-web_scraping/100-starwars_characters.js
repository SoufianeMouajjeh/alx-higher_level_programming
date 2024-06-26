#!/usr/bin/node
/*
 * This script sends a request to a URL
 * and prints the names of the characters
 * of a Star Wars movie
 */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  JSON.parse(body).characters.forEach(function (url, callback) {
    request(url, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
