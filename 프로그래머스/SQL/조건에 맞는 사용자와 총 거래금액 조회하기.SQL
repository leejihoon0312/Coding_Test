-- 코드를 입력하세요

select USER_ID, NICKNAME,	TOTAL_SALES

from

(SELECT *,sum(PRICE) as TOTAL_SALES
from USED_GOODS_BOARD
where STATUS = "DONE"
group by WRITER_ID
having sum(PRICE) >=700000) as sales

join

(select *
from USED_GOODS_USER ) as USERS

ON USERS.USER_ID =  sales.WRITER_ID

ORDER BY TOTAL_SALES