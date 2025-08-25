import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import warnings
import os

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from catboost import CatBoostRegressor
from sklearn.tree import DecisionTreeRegressor

warnings.filterwarnings("ignore")

# ---------- Data Preparation ----------
def prepare_and_save_data():
    df_soil = pd.read_csv("ClimateData/sensors_data.csv", sep=";")
    df_air = pd.read_csv("ClimateData/weather_data.csv", sep=";")
    dist = [['tinovi-01', 40], ['tinovi-02', 16], ['tinovi-03', 330],
            ['tinovi-04', 240], ['tinovi-05', 90], ['tinovi-06', 65],
            ['tinovi-07', 170], ['tinovi-08', 340]]
    dfdist = pd.DataFrame(dist, columns=['nodeid', 'distance'])

    df_soil = df_soil.sort_values('timestamp')
    df_air = df_air.sort_values('Timestamp')
    df_soil.rename(columns={'timestamp': 'Timestamp'}, inplace=True)
    merged_df = pd.merge_asof(df_soil, df_air, on='Timestamp', direction='nearest', tolerance=300)
    merged_df = merged_df.merge(dfdist, how='left', on='nodeid')

    if 'spreading_factor' in merged_df.columns:
        merged_df.drop(columns=['spreading_factor'], inplace=True)
    merged_df = merged_df.dropna(subset=['gtw_snr', 'frequency'])

    os.makedirs("ClimateData", exist_ok=True)
    merged_df.to_csv("ClimateData/dftobeloaded.csv", index=False)
    print(f"Saved processed data to: ClimateData/dftobeloaded.csv")

# ---------- Modeling & Plotting ----------
def get_model(name):
    if name == 'Random Forest':
        return RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    elif name == 'XGBoost':
        return XGBRegressor(learning_rate=0.1, max_depth=10, n_estimators=100, random_state=42)
    elif name == 'Gradient Boosting':
        return GradientBoostingRegressor(n_estimators=100, random_state=42)
    elif name == 'CatBoost':
        return CatBoostRegressor(depth=10, iterations=1000, learning_rate=0.05, random_seed=42, silent=True)
    elif name == 'Decision Tree':
        return DecisionTreeRegressor(max_depth=10, random_state=42)
    elif name == 'Linear Regression':
        return LinearRegression()
    else:
        raise ValueError(f"Model name '{name}' not recognized.")

def get_pov(pred, actual):
    ss_res = np.sum((actual - pred) ** 2)
    ss_tot = np.sum((actual - np.mean(actual)) ** 2)
    return 1 - (ss_res / ss_tot)

def run_simulation(df, feature_list, target, model_name, results_file):
    X = df[feature_list]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    model = get_model(model_name)

    start = time.time()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    elapsed = time.time() - start

    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    pov = get_pov(predictions, y_test)
    r2 = r2_score(y_test, predictions)

    line = f"{'+'.join(feature_list)},{model_name},{pov},{rmse},{r2},{elapsed}\n"
    with open(results_file, 'a') as fp:
        fp.write(line)
    print(f"{model_name} | {feature_list} | RMSE: {rmse:.4f} | POV: {pov:.4f}")

def plot_model_comparison(results_file):
    df = pd.read_csv(results_file, header=None)
    df.columns = ['Features', 'Model', 'POV', 'RMSE', 'R2', 'Time']

    os.makedirs("ClimateData/graphs", exist_ok=True)

    plt.figure(figsize=(12, 6))
    sns.barplot(x='Model', y='RMSE', hue='Features', data=df)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("ClimateData/graphs/rmse_comparison.png", dpi=300)
    plt.close()

    sns.barplot(x='Model', y='POV', hue='Features', data=df)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("ClimateData/graphs/pov_comparison.png", dpi=300)
    plt.close()

    print("Graphs saved to ClimateData/graphs/")

# ---------- Main Pipeline ----------
def main():
    prepare_and_save_data()
    df = pd.read_csv("ClimateData/dftobeloaded.csv")

    results_file = "ClimateData/resSNR.txt"
    if os.path.exists(results_file):
        os.remove(results_file)

    feature_sets = [
        ['frequency'],
        ['frequency', 'soil_temp', 'soil_hum'],
        ['frequency', 'Temp', 'Hum', 'Bar'],
        ['frequency', 'Temp', 'Hum', 'soil_temp', 'soil_hum', 'Bar'],
        ['frequency', 'distance'],
        ['frequency', 'distance', 'soil_temp', 'soil_hum'],
        ['frequency', 'distance', 'Temp', 'Hum', 'Bar'],
        ['frequency', 'distance', 'Temp', 'Hum', 'soil_temp', 'soil_hum', 'Bar'],
        ['frequency', 'gtw_rssi'],
        ['frequency', 'gtw_rssi', 'soil_temp', 'soil_hum'],
        ['frequency', 'gtw_rssi', 'Temp', 'Hum', 'Bar'],
        ['frequency', 'gtw_rssi', 'Temp', 'Hum', 'soil_temp', 'soil_hum', 'Bar'],
        ['frequency', 'distance', 'gtw_rssi'],
        ['frequency', 'distance', 'gtw_rssi', 'soil_temp', 'soil_hum'],
        ['frequency', 'distance', 'gtw_rssi', 'Temp', 'Hum', 'Bar'],
        ['frequency', 'distance', 'gtw_rssi', 'Temp', 'Hum', 'soil_temp', 'soil_hum', 'Bar']
    ]

    models = ['Random Forest', 'Gradient Boosting', 'XGBoost', 'CatBoost', 'Decision Tree', 'Linear Regression']

    for features in feature_sets:
        for model_name in models:
            run_simulation(df, features, 'gtw_snr', model_name, results_file)

    plot_model_comparison(results_file)

if __name__ == '__main__':
    main()
