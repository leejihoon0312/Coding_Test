-- 코드를 입력하세요
SELECT DATE_FORMAT(SALES_DATE,"%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE SUBSTRING_INDEX(SALES_DATE,"-",2) = "2022-03"
union
SELECT DATE_FORMAT(SALES_DATE,"%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE SUBSTRING_INDEX(SALES_DATE,"-",2) = "2022-03"
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID