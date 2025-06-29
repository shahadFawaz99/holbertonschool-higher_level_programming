-- Script to count shows by genre using JOIN, COUNT and GROUP BY
-- This script displays genre name and number of shows linked to each genre

-- Count shows by genre using JOIN, COUNT and GROUP BY
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres 
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
GROUP BY tv_genres.id, tv_genres.name
ORDER BY number_of_shows DESC;
