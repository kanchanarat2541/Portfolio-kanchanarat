CREATE External TABLE  demo_raw_zone.orders (
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
  's3://ijdhad-mydemo/raw_zone/orders/'