import sys
import boto3
import time
from datetime import datetime
# Create the Athena client
athena_client = boto3.client('athena', region_name='ap-southeast-1')

#day = datetime.today().strftime("%Y%m%d")
day = '19980506'
database = 'demo_landing_zone'
query = """
        alter table orders set location 's3://ijdhad-mydemo/landing_zone/orders/{}'
        """.format(day)

# Submit the query
response = athena_client.start_query_execution(
    QueryString=query,
    QueryExecutionContext={
        'Database': database
    },
    ResultConfiguration={
        'OutputLocation': 's3://ijdhad-mydemo/glue'
    }
)
 

