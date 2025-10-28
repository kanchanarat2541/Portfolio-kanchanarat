CREATE EXTERNAL TABLE  demo_raw_zone.products(
  productid bigint, 
  productname string, 
  supplierid bigint, 
  categoryid bigint, 
  quantityperunit string, 
  unitprice double, 
  unitsinstock bigint, 
  unitsonorder bigint, 
  reorderlevel bigint, 
  discontinued bigint)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
)
LOCATION
  's3://ijdhad-mydemo/raw_zone/products/'