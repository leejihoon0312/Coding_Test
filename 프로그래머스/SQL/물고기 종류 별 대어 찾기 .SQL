SELECT ID,	FISH_NAME,	LENGTH
FROM FISH_INFO AS FI JOIN FISH_NAME_INFO AS FNI ON FNI.FISH_TYPE = FI.FISH_TYPE
WHERE ( FNI.FISH_TYPE, LENGTH) IN (SELECT FISH_TYPE, MAX(LENGTH)
                                FROM FISH_INFO
                                GROUP BY FISH_TYPE)
ORDER BY ID
