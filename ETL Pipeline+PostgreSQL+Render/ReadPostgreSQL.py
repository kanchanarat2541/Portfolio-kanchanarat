import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# โหลดตัวแปรจาก .env
load_dotenv('.env')
db_url = os.getenv('DB_URL')
engine = create_engine(db_url)

# ดึงข้อมูลจากตาราง PostgreSQL (ตาราง Logging)
df = pd.read_sql(
    'SELECT * FROM weather_hourly_log ORDER BY forecast_time DESC LIMIT 100;',
    con=engine
)

print(df.head())  # แสดงข้อมูลล่าสุดที่ดึงจากฐานข้อมูลจริง

