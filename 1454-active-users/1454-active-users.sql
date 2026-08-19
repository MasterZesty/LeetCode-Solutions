# Write your MySQL query statement below
-- Approch 1: hard coded 
-- with count_of_daily_logins as (
-- select
-- id,
-- login_date,
-- count(login_date) as daily_login_count
-- from
-- logins
-- group by
-- id,
-- login_date
-- )

-- , active_user_stg as( 
-- select
-- id,
-- login_date as 1_login,
-- LEAD(login_date,1) OVER(PARTITION BY id ORDER BY login_date) as 2_login,
-- LEAD(login_date,2) OVER(PARTITION BY id ORDER BY login_date) as 3_login,
-- LEAD(login_date,3) OVER(PARTITION BY id ORDER BY login_date) as 4_login,
-- LEAD(login_date,4) OVER(PARTITION BY id ORDER BY login_date) as 5_login
-- from
-- count_of_daily_logins
-- )

-- select 
-- DISTINCT
-- a.id, 
-- b.name 
-- from active_user_stg a
-- left join accounts b
-- on a.id = b.id
-- where
-- DATE_ADD(1_login, INTERVAL 1 DAY) = 2_login AND
-- DATE_ADD(2_login, INTERVAL 1 DAY) = 3_login AND
-- DATE_ADD(3_login, INTERVAL 1 DAY) = 4_login AND
-- DATE_ADD(4_login, INTERVAL 1 DAY) = 5_login


-- Apporch 2: magic even i will not understand in future what is this spell i catsed at 2 in the night
-- with count_of_daily_logins as (
-- select
-- id,
-- login_date,
-- count(login_date) as daily_login_count
-- from
-- logins
-- group by
-- id,
-- login_date
-- )

-- , magic_abomination as (
-- select
-- id,
-- login_date,
-- -- MIN(login_date) OVER(PARTITION BY id) as min_login_date,
-- DATEDIFF(DATE_ADD(MIN(login_date) OVER(PARTITION BY id), INTERVAL ROW_NUMBER() OVER(PARTITION BY id ORDER BY login_date)DAY), login_date) as grp_dif
-- from
-- count_of_daily_logins
-- )

-- , abra_ka_dabra as (
-- select
-- id, 
-- count(grp_dif) as continue_logins
-- from
-- magic_abomination
-- group by
-- id,
-- grp_dif
-- having continue_logins >= 5 -- n can be anything
-- )

-- select distinct
-- a.id,
-- b.name
-- from abra_ka_dabra a
-- inner join Accounts b
-- on a.id = b.id
-- order by id

-- Apporch 3 : this is what gpt suggested
WITH daily_logins AS (
    SELECT DISTINCT
        id,
        login_date
    FROM logins
),

login_sequence AS (
    SELECT
        id,
        login_date,
        DATE_SUB(
            login_date,
            INTERVAL ROW_NUMBER() OVER (
                PARTITION BY id
                ORDER BY login_date
            ) DAY
        ) AS grp
    FROM daily_logins
),

login_streaks AS (
    SELECT
        id,
        grp
    FROM login_sequence
    GROUP BY
        id,
        grp
    HAVING COUNT(*) >= 5
)

SELECT DISTINCT
    s.id,
    a.name
FROM login_streaks s
JOIN accounts a
    ON s.id = a.id
ORDER BY s.id