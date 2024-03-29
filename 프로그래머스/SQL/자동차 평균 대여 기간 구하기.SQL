SELECT car_id, ROUND(AVG(RENTAL_DAY),1) AS AVERAGE_DURATION

FROM

(SELECT *, DATEDIFF(END_DATE,START_DATE)+1 AS RENTAL_DAY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) AS HISTORY

GROUP BY car_id

HAVING AVG(RENTAL_DAY) >= 7

ORDER BY AVERAGE_DURATION DESC , car_id DESC