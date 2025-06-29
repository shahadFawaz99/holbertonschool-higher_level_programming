-- Script to list all Comedy shows using multiple JOINs
-- This script displays tv_shows.title for Comedy genre shows

-- Select Comedy shows using multiple JOINs
SELECT tv_shows.title 
FROM tv_shows 
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id 
WHERE tv_genres.name = 'Comedy' 
ORDER BY tv_shows.title;
