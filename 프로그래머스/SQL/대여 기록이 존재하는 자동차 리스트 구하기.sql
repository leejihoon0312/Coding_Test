select distinct CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in (SELECT CAR_ID
                from CAR_RENTAL_COMPANY_CAR
                where CAR_TYPE = "세단") and date_format(start_date,"%m") = "10"
order by CAR_ID desc