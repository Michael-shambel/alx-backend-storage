-- script that list all bands with Glam rock as main style 
-- ranked by their longitativity 

SELECT band_name, IFNULL(
    CASE
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END,
    0
) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;