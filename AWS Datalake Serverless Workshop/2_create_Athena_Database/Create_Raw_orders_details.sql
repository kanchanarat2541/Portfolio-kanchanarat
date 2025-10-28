CREATE External TABLE  demo_raw_zone.orders_details (
  orderid bigint, 
  productid bigint, 
  unitprice double, 
  quantity bigint, 
  discount double)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
)
LOCATION
  's3://ijdhad-mydemo/raw_zone/orders_details/'