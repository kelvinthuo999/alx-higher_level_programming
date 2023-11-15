-- list all the genres and number of shows linked to each
SELECT name AS 'genre', count(genre_id) AS 'number_of_shows'
FROM tv_show_genres INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
