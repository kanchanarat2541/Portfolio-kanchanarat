CREATE TABLE demo_temp_zone.categories
WITH (
  format = 'PARQUET',
  parquet_compression = 'SNAPPY',
  external_location = 's3://ijdhad-mydemo/raw_zone/categories'
)
AS
SELECT
  categoryid, 
  categoryname, 
  description, 
  picture
FROM
  demo_landing_zone.categories

drop table  demo_temp_zone.categories