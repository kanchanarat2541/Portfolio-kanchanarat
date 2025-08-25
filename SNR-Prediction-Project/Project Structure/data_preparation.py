import pandas as pd
import os

def load_and_merge_sensor_data(soil_path, air_path, distance_data):
    df_soil = pd.read_csv(soil_path, sep=";")
    df_air = pd.read_csv(air_path, sep=";")
    
    df_soil = df_soil.sort_values('timestamp')
    df_air = df_air.sort_values('Timestamp')
    df_soil.rename(columns={'timestamp': 'Timestamp'}, inplace=True)

    merged_df = pd.merge_asof(df_soil, df_air, on='Timestamp', direction='nearest', tolerance=300)
    merged_df = merged_df.merge(distance_data, how='left', on='nodeid')

    if 'spreading_factor' in merged_df.columns:
        merged_df.drop(columns=['spreading_factor'], inplace=True)

    merged_df = merged_df.dropna(subset=['gtw_snr', 'frequency'])
    return merged_df

def save_processed_data(df, output_path="ClimateData/dftobeloaded.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved processed data to {output_path}")
