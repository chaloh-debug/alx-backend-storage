-- list bands with glam rock as their main style
-- order by their longetivity
SELECT band_name, (IFNULL(split, 2023) - formed) AS lifespan FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;