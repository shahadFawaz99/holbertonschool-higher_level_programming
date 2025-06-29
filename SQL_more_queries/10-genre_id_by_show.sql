-- Script to list all shows with their genre IDs using JOIN
-- This script displays tv_shows.title - tv_show_genres.genre_id

-- Select shows with their genre IDs using JOIN
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title, tv_show_genres.genre_id;
