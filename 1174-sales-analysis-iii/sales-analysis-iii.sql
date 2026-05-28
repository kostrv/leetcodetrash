# Write your MySQL query statement below




-- select
--     s.product_id,
--     p.product_name
-- from Sales s
-- left join Product p using(product_id)
-- where product_id in
--     (select 
--         product_id
--     from Sales 
--     group by product_id
--     having count(*) = 1
-- ) and sale_date between '2019-01-01' and '2019-03-31'


select product_id, product_name
from Product
where product_id in (
    select product_id from Sales where sale_date between '2019-01-01' AND '2019-03-31'
)
AND product_id NOT IN (
    select product_id from Sales where sale_date NOT between '2019-01-01' AND '2019-03-31'
);