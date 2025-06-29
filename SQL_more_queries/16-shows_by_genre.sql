-- Script to list all shows with their genres using LEFT JOIN
-- This script displays tv_shows.title - tv_genres.name (NULL if no genre)

-- Select all shows with their genres using LEFT JOIN
SELECT tv_shows.title, tv_genres.name 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id 
ORDER BY tv_shows.title, tv_genres.name;
