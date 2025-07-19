import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv('.env')
db_url = os.getenv('DB_URL')
engine = create_engine(db_url)

# ดึงข้อมูล
df = pd.read_sql('SELECT * FROM weather_hourly_log ORDER BY forecast_time DESC;', con=engine)

# บันทึกเป็น CSV
df.to_csv('weather_data.csv', index=False)
print('ข้อมูลถูกบันทึกเป็นไฟล์ CSV เรียบร้อยแล้ว')
