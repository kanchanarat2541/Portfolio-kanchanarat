CREATE TABLE demo_temp_zone.orders
WITH (
  format = 'PARQUET',
  parquet_compression = 'SNAPPY',
  external_location = 's3://ijdhad-mydemo/raw_zone/orders/1998/199805/19980505'
)
AS
SELECT
  orderid,
  customerid,
  employeeid,
  orderdate,
  requireddate,
  shippeddate,
  shipvia,
  freight,
  shipname,
  shipaddress,
  shipcity,
  shipregion,
  shippostalcode,
  shipcountry,
 '1998' AS year,
 '199805' AS month,
 '19980505' AS day
FROM
  demo_landing_zone.orders


ALTER TABLE demo_raw_zone.orders
ADD PARTITION (year='1998', month='199805', day='19980505')
LOCATION 's3://ijdhad-mydemo/raw_zone/orders/1998/199805/19980505';

drop table demo_temp_zone.orders