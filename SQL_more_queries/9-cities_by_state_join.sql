-- Select city id, city name, and state name
SELECT cities.id, cities.name, states.name
FROM cities
-- Join states table on cities.state_id to states.id
JOIN states ON cities.state_id = states.id
-- Order results by city id in ascending order
ORDER BY cities.id ASC;
