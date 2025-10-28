CREATE TABLE demo_temp_zone.orders_details
WITH (
  format = 'PARQUET',
  parquet_compression = 'SNAPPY',
  external_location = 's3://ijdhad-mydemo/raw_zone/orders_details'
)
AS
SELECT
  orderid, 
  productid, 
  unitprice, 
  quantity, 
  discount
FROM
  demo_landing_zone.orders_details


drop table  demo_temp_zone.orders_details