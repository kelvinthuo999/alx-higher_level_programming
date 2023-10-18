-- List all cities of California

SELECT cities.* FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;
