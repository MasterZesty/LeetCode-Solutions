# Write your MySQL query statement below

-- STEP 1 : understand
-- select
-- content_id,
-- content_text,
-- REGEXP_SUBSTR(content_text, '[a-zA-Z]+|-', 1, 1) AS word, 
-- 1 AS word_position
-- from user_content where content_id = 1
-- union all
-- select
-- content_id,
-- content_text,
-- REGEXP_SUBSTR(content_text, '[a-zA-Z]+|-', 1, 2) AS word, 
-- 1 AS word_position
-- from user_content where content_id = 1
-- union all
-- select
-- content_id,
-- content_text,
-- REGEXP_SUBSTR(content_text, '[a-zA-Z]+|-', 1, 3) AS word, 
-- 1 AS word_position
-- from user_content where content_id = 1
-- union all
-- select
-- content_id,
-- content_text,
-- REGEXP_SUBSTR(content_text, '[a-zA-Z]+|-', 1, 4) AS word, 
-- 1 AS word_position
-- from user_content where content_id = 1
-- union all
-- select
-- content_id,
-- content_text,
-- REGEXP_SUBSTR(content_text, '[a-zA-Z]+|-', 1, 5) AS word, 
-- 1 AS word_position
-- from user_content where content_id = 1

-- REGEXP_SUBSTR(expr, pat, pos, occurrence)

with RECURSIVE rcte as (
select
content_id,
content_text,
REGEXP_SUBSTR(content_text, '[a-zA-Z]+|-', 1, 1) AS word, 
1 AS word_position
from user_content where REGEXP_SUBSTR(content_text, '[a-zA-Z]+|-', 1, 1) IS NOT NULL
union all
select
content_id,
content_text,
REGEXP_SUBSTR(content_text, '[a-zA-Z]+|-', 1, word_position + 1) AS word, 
word_position + 1 AS word_position
from rcte where REGEXP_SUBSTR(content_text, '[a-zA-Z]+|-', 1, word_position + 1) IS NOT NULL
),

cte as (
select
content_id,
content_text,
word,
CONCAT( UPPER(SUBSTRING(word,1,1)), LOWER(SUBSTRING(word,2,LENGTH(word)-1)) ) as word2,
word_position
from rcte
),

cte2 as (
select
content_id,
content_text as original_text,
GROUP_CONCAT( word2 ORDER BY word_position SEPARATOR ' ') as converted_text
-- COUNT(word2) AS converted_text
from 
cte
group by
content_id,
content_text
)

select
content_id,
original_text,
REPLACE(converted_text, ' - ', '-') as converted_text
-- COUNT(word2) AS converted_text
from 
cte2
