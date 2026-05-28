# Write your MySQL query statement below


-- select  
--     product_id,
--     first_year
--     quantity,
--     price
-- from (
--     select 
--         product
--     from Sales s 
-- ) 



select  
    s1.product_id,
    s1.year as first_year,
    s1.quantity,
    s1.price
from Sales s1
inner join 
( select 
    product_id,
    MIN(year) as first_year
from Sales s
group by product_id 
) t on t.product_id = s1.product_id and t.first_year = s1.year
