-- Script to list all shows without genres using LEFT JOIN and WHERE
-- This script displays tv_shows.title - tv_show_genres.genre_id for shows without genres

-- Select shows without genres using LEFT JOIN and WHERE
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
