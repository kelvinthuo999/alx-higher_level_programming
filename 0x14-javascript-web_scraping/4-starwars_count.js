#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const filmsData = JSON.parse(body);
    const moviesWithWedgeAntilles = filmsData.results.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)
    );

    console.log(moviesWithWedgeAntilles.length);
  }
});
