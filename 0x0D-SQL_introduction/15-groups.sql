-- count 
SELECT score ,COUNT(*)
FROM second_table
ORDER score BY DESC
GROUP BY score 