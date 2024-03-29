-- 코드를 입력하세요

SELECT FLAVOR

FROM

(select JULY.FLAVOR, HALF.TOTAL_ORDER+JULY.7TOTAL AS RESULT

from

(select *
from FIRST_HALF) as HALF

left join

(SELECT FLAVOR, sum(TOTAL_ORDER) AS "7TOTAL"
from JULY
group by FLAVOR) AS JULY

ON HALF.FLAVOR = JULY.FLAVOR

ORDER BY RESULT DESC

LIMIT 3) AS LAST

