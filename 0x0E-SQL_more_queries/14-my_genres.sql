-- not empty
-- file
SELECT tvg.name FROM tvshows tv INNER JOIN tv_show_genres tvsg ON tv.id = tvsg.show_id INNER JOIN tv_genres tvg ON tvsg.genre_id = tvg.id WHERE tv.title = 'Dexter' ORDER BY tvg.name ASC;
