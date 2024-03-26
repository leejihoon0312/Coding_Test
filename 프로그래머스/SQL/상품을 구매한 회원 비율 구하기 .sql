select year(SALES_DATE) as YEAR, month(SALES_DATE) as MONTH, count(distinct USER_ID) as PUCHASED_USERS ,
round(count(distinct USER_ID)/(SELECT count(*)
from USER_INFO
where year(JOINED) = 2021),1) as PUCHASED_RATIO

from ONLINE_SALE

where USER_ID in (SELECT USER_ID
                from USER_INFO
                where year(JOINED) = 2021)

group by year(SALES_DATE), month(SALES_DATE)

order by YEAR, MONTH