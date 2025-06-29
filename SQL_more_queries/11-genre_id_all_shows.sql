-- Select all shows and their genre ids (if any)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Use LEFT JOIN to include shows without genres (genre_id will be NULL)
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
