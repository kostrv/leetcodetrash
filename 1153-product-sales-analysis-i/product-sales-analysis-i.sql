# Write your MySQL query statement below




select 
     product_name,
     year ,
     price
from Product p
inner join Sales s using (product_id) 