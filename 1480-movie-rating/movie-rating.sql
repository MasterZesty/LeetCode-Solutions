# Write your MySQL query statement below
WITH user_ranked AS (
    SELECT
        u.name,
        ROW_NUMBER() OVER (
            ORDER BY COUNT(*) DESC, u.name ASC
        ) AS rn
    FROM MovieRating mr
    JOIN Users u
        ON mr.user_id = u.user_id
    GROUP BY u.user_id, u.name
),

movie_ranked AS (
    SELECT
        m.title,
        ROW_NUMBER() OVER (
            ORDER BY AVG(mr.rating) DESC, m.title ASC
        ) AS rn
    FROM MovieRating mr
    JOIN Movies m
        ON mr.movie_id = m.movie_id
    WHERE mr.created_at >= '2020-02-01'
      AND mr.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
)

SELECT name AS results
FROM user_ranked
WHERE rn = 1

UNION ALL

SELECT title AS results
FROM movie_ranked
WHERE rn = 1;