import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_feature_sets(df):
    # ตัวอย่างการสร้างชุดฟีเจอร์ (ปรับตามข้อมูลจริง)
    feature_sets = [
        ['frequency'],
        ['frequency', 'soil_temp', 'soil_hum'],
        ['frequency', 'Temp', 'Hum', 'Bar'],
        ['frequency', 'distance', 'gtw_rssi', 'soil_temp', 'soil_hum', 'Temp', 'Hum', 'Bar'],
        # เพิ่มชุดฟีเจอร์อื่น ๆ ตามต้องการ
    ]
    return feature_sets

def plot_correlation_pairgrid(df, columns, labels, save_path):
    sns.set(style="ticks")
    g = sns.pairplot(df[columns].rename(columns=dict(zip(columns, labels))))
    g.fig.suptitle("Feature Correlation PairGrid", y=1.02)
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Saved correlation plot to {save_path}")

def plot_feature_importance(importance_dict, save_path):
    features = list(importance_dict.keys())
    importances = list(importance_dict.values())
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances, y=features)
    plt.title("Feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("Features")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Saved feature importance plot to {save_path}")

def run_analysis():
    df = pd.read_csv("/content/drive/My Drive/ClimateData/dftobeloaded.csv")
    
    feature_sets = generate_feature_sets(df)

    plot_correlation_pairgrid(
        df,
        columns=['gtw_snr','frequency','distance','gtw_rssi','Temp','Hum','soil_temp','soil_hum','Bar'],
        labels=['SNR','Frequency','Distance','RSSI','Air Temp','Air Humidity','Soil Temp','Soil Humidity','Pressure'],
        save_path="/content/drive/My Drive/ClimateData/correlation_plot.png"
    )

    importance_dict = {
        'frequency': 0.3,
        'gtw_rssi': 0.2,
        'soil_temp': 0.15,
        'soil_hum': 0.1,
        'Temp': 0.1,
        'Hum': 0.05,
        'Bar': 0.05,
        'distance': 0.05
    }

    plot_feature_importance(importance_dict, save_path="/content/drive/My Drive/ClimateData/feature_importance.png")

if __name__ == "__main__":
    run_analysis()

