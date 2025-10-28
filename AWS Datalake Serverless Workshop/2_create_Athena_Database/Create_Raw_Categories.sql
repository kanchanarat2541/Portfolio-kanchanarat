CREATE EXTERNAL TABLE demo_raw_zone.categories(
  categoryid bigint, 
  categoryname string, 
  description string, 
  picture string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
)
LOCATION
   's3://ijdhad-mydemo/raw_zone/categories/'