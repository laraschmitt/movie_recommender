
SELECT COUNT (DISTINCT title) AS "distinct movie titles in movies table" 
FROM movies;
--58020


SELECT COUNT (DISTINCT movieid) AS "distinct movie ids in movies table" 
FROM movies;
--58098
-- less movie titles than movieIds
-- some movies have more than one ID assigned

SELECT
  title,
  count(*)
FROM movies
GROUP BY
  title
HAVING count(*) > 1;

SELECT * FROM movies
LIMIT 100;