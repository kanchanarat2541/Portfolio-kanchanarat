CREATE TABLE demo_temp_zone.customers
WITH (
  format = 'PARQUET',
  parquet_compression = 'SNAPPY',
  external_location = 's3://ijdhad-mydemo/raw_zone/customers'
)
AS
SELECT
  customerid , 
  companyname , 
  contactname , 
  contacttitle , 
  address , 
  city , 
  region , 
  postalcode , 
  country , 
  phone , 
  fax
FROM
  demo_landing_zone.customers

drop table demo_temp_zone.customers