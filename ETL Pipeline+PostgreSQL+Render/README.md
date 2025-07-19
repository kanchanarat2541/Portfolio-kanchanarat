# 🌤️ Weather ETL Pipeline with PostgreSQL on Render

A simple ETL pipeline project that:
- Extracts hourly weather forecast data from a public API
- Transforms and cleans the data
- Loads the data into a PostgreSQL cloud database hosted on Render.com
- Designed as a Time Series Logging System

---

## 📊 Project Overview

| Pipeline Stage | Description |
|----------------|-------------|
| **Extract**    | Pull hourly temperature forecasts via [Open-Meteo API](https://open-meteo.com/en) |
| **Transform**  | Clean and format the data (forecast time, temperature, fetch time) |
| **Load**       | Save into a cloud PostgreSQL database using SQLAlchemy |

Collected data can later be visualized using Power BI, Metabase, or other dashboard tools.

---

## 🛠️ Technologies Used

- **Python** (requests, pandas, SQLAlchemy, dotenv)
- **PostgreSQL** (Database hosted on [Render.com](https://render.com/))
- **Render.com** (as a free cloud PostgreSQL provider)
- Optional visualization via Power BI / Google Data Studio

---

## ⚙️ How It Works

1. Connects to the Open-Meteo weather forecast API
2. Stores:
   - `forecast_time`: the time of the forecasted weather
   - `fetch_time`: the timestamp of when the API was called
   - `temperature`: hourly temperature forecast
3. Saves the data into the table `weather_hourly_log` in PostgreSQL

---

## 🏗️ Database Schema

```sql
CREATE TABLE weather_hourly_log (
    id SERIAL PRIMARY KEY,
    forecast_time TIMESTAMP NOT NULL,
    fetch_time TIMESTAMP NOT NULL,
    temperature FLOAT,
    location VARCHAR(100) DEFAULT 'Bangkok'
);
