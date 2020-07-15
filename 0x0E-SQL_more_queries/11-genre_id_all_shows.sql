-- The last defender of the sprawl/said, well where do you kids live?
-- well sir, if you only knew/what the answer is worth/been searching every corner/of the earth
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
