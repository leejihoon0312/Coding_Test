-- 코드를 입력하세요


select ANIMAL_ID, NAME

from ANIMAL_OUTS

where ANIMAL_ID not in (SELECT INS.ANIMAL_ID

from

(select ANIMAL_ID
from ANIMAL_INS) as INS

join

(select ANIMAL_ID
from ANIMAL_OUTS) as OUTS

on INS.ANIMAL_ID = OUTS.ANIMAL_ID)

order by ANIMAL_ID

