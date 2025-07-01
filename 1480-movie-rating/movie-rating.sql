-- Top user by number of ratings
(SELECT u.name AS results
 FROM MovieRating mr
 JOIN Users u ON mr.user_id = u.user_id
 GROUP BY mr.user_id
 ORDER BY COUNT(mr.movie_id) DESC, u.name ASC
 LIMIT 1)

UNION ALL

-- Top movie by avg rating in Feb 2020
(SELECT m.title AS results
 FROM MovieRating mr
 JOIN Movies m ON mr.movie_id = m.movie_id
 WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
 GROUP BY mr.movie_id
 ORDER BY AVG(mr.rating) DESC, m.title ASC
 LIMIT 1);
