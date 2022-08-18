#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200) {
    const charactersList = JSON.parse(body).characters;
    for (const link of charactersList) {
      request(link, function (err, resp, body) {
        if (err) {
          console.log(err);
        } else if (resp.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
