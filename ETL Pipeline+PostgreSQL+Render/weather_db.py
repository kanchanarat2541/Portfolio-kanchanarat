import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from dotenv import load_dotenv
import os

# โหลดตัวแปรจาก .env
load_dotenv('.env')
db_url = os.getenv('DB_URL')

# STEP 1: Extract
def fetch_weather_data():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=13.75&longitude=100.5&hourly=temperature_2m'
    response = requests.get(url)
    data = response.json()
    hourly_data = data['hourly']
    df = pd.DataFrame({
        'forecast_time': hourly_data['time'],   # ชื่อให้ตรงกับตาราง
        'temperature': hourly_data['temperature_2m']
    })
    return df

# STEP 2: Transform
def transform_data(df):
    df['forecast_time'] = pd.to_datetime(df['forecast_time'])
    df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
    df.drop_duplicates(subset=['forecast_time'], inplace=True)
    df = df.dropna()
    return df

# STEP 3: Load
def load_to_db(df):
    engine = create_engine(db_url)
    fetch_time = datetime.now()
    df['fetch_time'] = fetch_time
    df['location'] = 'Bangkok'

    df.to_sql('weather_hourly_log', con=engine, if_exists='append', index=False)
    print(f"[{fetch_time}] Data inserted: {len(df)} records.")

# MAIN
def main():
    df_raw = fetch_weather_data()
    df_clean = transform_data(df_raw)
    load_to_db(df_clean)

if __name__ == '__main__':
    main()
