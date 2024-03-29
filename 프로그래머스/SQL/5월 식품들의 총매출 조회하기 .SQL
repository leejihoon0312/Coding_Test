-- 코드를 입력하세요

select FOOD_PRODUCT.PRODUCT_ID, PRODUCT_NAME, AMOUNT*PRICE AS TOTAL_SALES

from

(SELECT PRODUCT_ID, sum(AMOUNT) AS AMOUNT
from FOOD_ORDER
where year(PRODUCE_DATE) = 2022 and month(PRODUCE_DATE) = 5
group by PRODUCT_ID) as ORDERS

join

(select *
from FOOD_PRODUCT) as FOOD_PRODUCT

on ORDERS.PRODUCT_ID = FOOD_PRODUCT.PRODUCT_ID

ORDER BY TOTAL_SALES DESC, PRODUCT_ID
