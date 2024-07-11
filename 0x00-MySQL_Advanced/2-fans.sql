-- script that ranks country by origins of bands
-- order bt the number of fans

SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
