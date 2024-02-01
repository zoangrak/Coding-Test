SELECT HISTORY_ID, 
    round(DAILY_FEE * (DATEDIFF(h.END_DATE, h.START_DATE)+1)
    * (case 
    when DATEDIFF(END_DATE, START_DATE) + 1 < 7 then 1
    when DATEDIFF(END_DATE, START_DATE) + 1 < 30 then 0.95
    when DATEDIFF(END_DATE, START_DATE) + 1 < 90 then 0.92
    else 0.85 end)) as "FEE"

FROM CAR_RENTAL_COMPANY_CAR as c 
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
    on c.CAR_ID = h.CAR_ID
    join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
    on c.CAR_TYPE = p.CAR_TYPE

WHERE c.car_type = "트럭"
GROUP BY HISTORY_ID
ORDER BY FEE DESC, HISTORY_ID DESC