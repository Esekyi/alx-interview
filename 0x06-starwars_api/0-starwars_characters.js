#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (let i = 0; i < characters.length; i++) {
      const url = characters[i];
      await new Promise((resolve, reject) => {
        request(url, function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            const data = JSON.parse(body);
            console.log(data.name);
          }
          resolve();
        });
      });
    }
  }
});
