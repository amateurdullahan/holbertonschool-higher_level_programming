-- Looking out for number one
-- California, here we come
SELECT 'cities'.id, cities.name
       FROM 'states', 'cities'
       WHERE cities.state_id == states.id
       AND states.name = 'California';
