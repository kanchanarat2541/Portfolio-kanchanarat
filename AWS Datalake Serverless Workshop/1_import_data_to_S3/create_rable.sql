CREATE External TABLE demo2.raw_orders (
  orderid bigint, 
  customerid string, 
  employeeid bigint, 
  orderdate string, 
  requireddate string, 
  shippeddate string, 
  shipvia bigint, 
  freight double, 
  shipname string, 
  shipaddress string, 
  shipcity string, 
  shipregion string, 
  shippostalcode string, 
  shipcountry string)
PARTITIONED BY (year string, month string, day string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
)
LOCATION
  's3://sdadaasaa/Landing_Zone/raw_orders/'



CREATE TABLE demo2.raw_orders_19980101
WITH (
  format = 'PARQUET',
  parquet_compression = 'SNAPPY',
  external_location = 's3://sdadaasaa/Landing_Zone/raw_orders/1998/199801/19980101'
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
  SUBSTR(orderdate, 1, 4) AS year,
  SUBSTR(orderdate, 6, 2) AS month,
  SUBSTR(orderdate, 9, 2) AS day
FROM
  demo2."temp_orders"


ALTER TABLE demo2.raw_orders
ADD PARTITION (year='1998', month='199801', day='19980102')
LOCATION 's3://sdadaasaa/Landing_Zone/raw_orders/1998/199801/19980102/';