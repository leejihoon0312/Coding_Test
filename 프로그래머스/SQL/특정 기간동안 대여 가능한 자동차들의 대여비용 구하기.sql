select *

from

(select CAR_ID,	borrow.CAR_TYPE, round(daily_fee*30*(1-(DISCOUNT_RATE/100))) as fee

from

(SELECT *
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE IN ('세단','SUV') and CAR_ID not in
(SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY

WHERE CAR_ID IN (SELECT CAR_ID
                FROM CAR_RENTAL_COMPANY_CAR
                WHERE CAR_TYPE IN ('세단','SUV'))
AND( ((START_DATE < "2022-11-01") AND ("2022-11-01" <= END_DATE)) OR (START_DATE BETWEEN "2022-11-01" AND "2022-11-30") ))) as borrow

join

(select CAR_TYPE, DISCOUNT_RATE
from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
where CAR_TYPE in ('세단','SUV') and DURATION_TYPE = "30일 이상") rate

on borrow.CAR_TYPE = rate.CAR_TYPE

order by fee desc, CAR_TYPE, CAR_ID desc) as last

where fee between 500000 and 1999999