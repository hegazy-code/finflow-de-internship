
CREATE TABLE t1 AS
         SELECT*
         FROM read_csv_auto("C:\Users\Yousssef\OneDrive\Desktop\finflow-de-internship\tramsaction.csv");
SELECT
         type,
         SUM(amount) AS total_transaction_volume
         from t1
         GROUP BY type;


 select
         type,
         QUANTILE_CONT(amount,0.90)AS percentile_90
         from t1
         GROUP BY type;

SELECT
         nameOrig,
         count(*)AS transaction_cout
         from t1
         GROUP BY nameOrig
         HAVING COUNT(*)>3;

select
   type,
        SUM(amount) over 
        from t1
   

    


select  count(*) AS full_drain_transaction, (SUM(case when Isfraud=1 then 1 else 0 end)* 100) / (count(*)) as fraud_transfer  from t1 where newbalanceOrig=0 AND oldbalanceOrg > 0;


create tabke t1,
 select*
 from read.csv(0)

 select
 type,
 sum(amount) as total_transaction_volume
 from t1


 select
 type,
   quantile_cont(amount,0.90) as percentile_90
 from t1
 select
 nameOrige
 count(*) as transaction_count
        from t1
        having count(*)>3


select
count(*)as full_drain_tramsaction,
sum(sum isfraud=1 then 1 else 0 end ) as fraund_transfer
(100*


