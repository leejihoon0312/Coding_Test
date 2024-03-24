-- 코드를 입력하세요

SELECT FEE.history_id, ROUND(daily_fee*PERIOD*(1-(discount_rate/100))) AS FEE

FROM

(select history_id, daily_fee
from CAR_RENTAL_COMPANY_CAR as CAR
join (select *
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in (SELECT CAR_ID
                from CAR_RENTAL_COMPANY_CAR
                where CAR_TYPE = "트럭")) as HISTORY
on CAR.CAR_ID = HISTORY.CAR_ID ) AS FEE

JOIN


(select history_id,	car_id,datediff(end_date,start_date)+1 AS PERIOD,IFNULL(discount_rate,0) AS discount_rate
from
(select *, datediff(end_date,start_date)+1,
(
    case
        when datediff(end_date,start_date)+1 >=90 then "90일 이상"
        when datediff(end_date,start_date)+1 >=30 then "30일 이상"
        when datediff(end_date,start_date)+1 >=7 then "7일 이상"
        else null
    end
) as duration_type
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in (SELECT CAR_ID
                from CAR_RENTAL_COMPANY_CAR
                where CAR_TYPE = "트럭")) as A
LEFT JOIN  (select *
from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
where car_type = "트럭") AS B

ON A.duration_type = B.duration_type) AS RATE

ON FEE.history_id = RATE.history_id

ORDER BY FEE DESC, FEE.history_id DESC