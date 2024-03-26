-- 코드를 입력하세요


select INS.ANIMAL_ID,	INS.ANIMAL_TYPE,	INS.NAME

from

(select *
from ANIMAL_INS) as INS

join

(select *
from ANIMAL_OUTS) as OUTS

on OUTS.ANIMAL_ID = INS.ANIMAL_ID

where (SEX_UPON_INTAKE not like "%Spayed%" and SEX_UPON_INTAKE not like "%Neutered%") and
(SEX_UPON_OUTCOME like "%Spayed%" or SEX_UPON_OUTCOME like "%Neutered%")

order by ANIMAL_ID