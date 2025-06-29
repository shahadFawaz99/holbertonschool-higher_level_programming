-- Select the id and name columns from the cities table
SELECT id, name
FROM cities
-- Filter cities that belong to the state of California using a subquery
WHERE state_id = (
    -- Subquery to get the id of the state named 'California' from the states table
    SELECT id FROM states WHERE name = 'California'
)
-- Order the results by city id in ascending order
ORDER BY id ASC;
