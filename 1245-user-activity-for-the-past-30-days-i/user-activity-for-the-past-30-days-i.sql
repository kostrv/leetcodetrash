-- -- # Write your MySQL query statement below

-- select 
--     activity_date AS 'day',
--     COUNT(distinct user_id) AS active_users
-- from Activity
-- where activity_date > 
--     (
--         SELECT DATE_SUB(MAX(activity_date), INTERVAL 30 DAY)
--         FROM Activity
--     )
-- group by activity_date




select 
    activity_date AS 'day',
    COUNT(distinct user_id) AS active_users
from Activity
where activity_date <= '2019-07-27'
AND activity_date > DATE_SUB('2019-07-27', INTERVAL 30 DAY) 
group by activity_date
