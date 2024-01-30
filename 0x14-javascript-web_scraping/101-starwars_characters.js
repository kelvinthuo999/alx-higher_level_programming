#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    // Function to fetch character names based on URLs
    const fetchCharacterNames = (urls) => {
      return new Promise((resolve, reject) => {
        const characterNames = [];

        const fetchNextCharacter = async (index) => {
          if (index < urls.length) {
            const characterUrl = urls[index];
            request(characterUrl, (characterError, characterResponse, characterBody) => {
              if (!characterError && characterResponse.statusCode === 200) {
                const characterData = JSON.parse(characterBody);
                characterNames.push(characterData.name);
                fetchNextCharacter(index + 1);
              } else {
                reject(new Error(`Failed to fetch character data. Status code: ${characterResponse ? characterResponse.statusCode : 'N/A'}`));
              }
            });
          } else {
            resolve(characterNames);
          }
        };

        fetchNextCharacter(0);
      });
    };

    // Fetch and display character names
    fetchCharacterNames(charactersUrls)
      .then((characterNames) => {
        characterNames.forEach((characterName) => {
          console.log(characterName);
        });
      })
      .catch((fetchError) => {
        console.error(fetchError.message);
      });
  } else {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
