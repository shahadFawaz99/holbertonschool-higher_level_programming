-- Script to list all shows with their genre IDs using LEFT JOIN
-- This script displays tv_shows.title - tv_show_genres.genre_id (NULL if no genre)

-- Select all shows with their genre IDs using LEFT JOIN
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title, tv_show_genres.genre_id;
