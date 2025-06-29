-- Select the show title and genre_id from the tv_shows and tv_show_genres tables
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Join the tv_show_genres table on show id
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
-- Order results by title then genre_id ascending
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
