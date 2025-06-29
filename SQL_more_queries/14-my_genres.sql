-- Script to list all genres of the show Dexter using multiple JOINs
-- This script displays tv_genres.name for the show Dexter

-- Select genres of Dexter using multiple JOINs
SELECT tv_genres.name 
FROM tv_shows 
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id 
WHERE tv_shows.title = 'Dexter' 
ORDER BY tv_genres.name;
