from sqlalchemy import create_engine, text
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv('.env')
db_url = os.getenv('DB_URL')
engine = create_engine(db_url)

create_table_sql = """
CREATE TABLE IF NOT EXISTS weather_hourly_log (
    id SERIAL PRIMARY KEY,
    forecast_time TIMESTAMP NOT NULL,
    fetch_time TIMESTAMP NOT NULL,
    temperature FLOAT,
    location VARCHAR(100) DEFAULT 'Bangkok'
);
"""

with engine.connect() as conn:
    conn.execute(text(create_table_sql))  
    print("Table created successfully.")