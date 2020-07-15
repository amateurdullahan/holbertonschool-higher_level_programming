-- I walk a lonely road
-- On this boulevard of broken dreams
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
