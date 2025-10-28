import sys
import boto3
import time
from datetime import datetime
# Create the Athena client
athena_client = boto3.client('athena', region_name='ap-southeast-1')

year = '1998'
month = '199805'
day = '19980506'
database = 'demo_raw_zone'
query_string = """
        CREATE TABLE demo_temp_zone.orders_{2}
        WITH (
          format = 'PARQUET',
          parquet_compression = 'SNAPPY',
          external_location = 's3://ijdhad-mydemo/raw_zone/orders/{0}/{1}/{2}'
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
        '{0}' AS year,
        '{1}' AS month,
        '{2}' AS day
        FROM
          demo_landing_zone.orders;
        ALTER TABLE demo_raw_zone.orders
        ADD PARTITION (year='{0}', month='{1}', day='{2}')
        LOCATION 's3://ijdhad-mydemo/raw_zone/orders/{0}/{1}/{2}/';
        DROP TABLE demo_temp_zone.orders_{2}
        """.format(year,month,day)

# Submit the query
query_list = query_string.split(";")
for query in query_list:
  response = athena_client.start_query_execution(
      QueryString=query,
      QueryExecutionContext={
          'Database': database
      },
      ResultConfiguration={
          'OutputLocation': 's3://ijdhad-mydemo/glue'
      }
    )
  query_execution_id = response['QueryExecutionId']
  status = None
  while status not in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
    response2 = athena_client.get_query_execution(
        QueryExecutionId=query_execution_id
    )
    status = response2['QueryExecution']['Status']['State']
    if status == 'SUCCEEDED':
        print("Query execution completed successfully.")
        break
    elif status in ['FAILED', 'CANCELLED']:
        print("Query execution failed or was cancelled.")
        break
    time.sleep(5)
  # Get the query execution ID
  query_execution_id = response['QueryExecutionId']
  print("Query Execution ID:", query_execution_id)




