📡 SNR Prediction Using Environmental Sensor Data
Predicts Signal-to-Noise Ratio (SNR) in wireless communication using machine learning models, based on environmental and sensor data such as temperature, humidity, pressure, and soil readings. Built as an end-to-end, modular Python pipeline.

📊 Project Overview
Objective: Predict SNR using environmental and signal-related features.
Dataset: Multi-source time-series data from weather and soil sensors.
Approach: Applied and compared multiple regression models for performance evaluation.
Best Result: CatBoost achieved ~76% Proportion of Variance (PoV).

⚙️ Key Features
Time-series sensor data merging and preprocessing.
Feature engineering from weather, soil, and signal data.
Regression model training using ensemble and boosting algorithms.
Model evaluation via RMSE, R², and PoV.
Visual comparison of model performances and feature importance.
Modular, reproducible Python pipeline.

🛠️ Tools & Libraries
Languages: Python

Libraries:
pandas, numpy (data processing)
scikit-learn (baseline models, preprocessing)
xgboost, catboost (boosting models)
matplotlib, seaborn (visualization)
Platform: Google Colab

📈 Machine Learning Models
Linear Regression
Decision Tree
Random Forest
Gradient Boosting
XGBoost
CatBoost

## 📊 Results & Improvements

| Version                  | Best Model  | PoV (%) |
|--------------------------|-------------|---------|
| Published (2025)         | XGBoost     | 73.00   |
| Current Project (2025)   | CatBoost    | 76.35   |

- The **published approach** achieved **~73% PoV** using XGBoost.
- The **current project** improved performance to **76.35% PoV** with CatBoost, reflecting enhanced feature use and tuning.

---
Project Structure
├── notebooks/           # Jupyter Notebooks for data exploration & modeling
├── src/                 # (Optional) Python scripts/modules
├── data/                # Sample or simulated datasets (not included)
├── images/              # Graphs and plots
├── README.md            # Project overview
├── requirements.txt     # List of Python dependencies


## 📄 Reference Publication

Apavatjrut, A., & Chokruay, K. (2025).  
**SNR Prediction Based on Environmental Sensing Data: An Approach Using Machine Learning.**  
*ECTI Transactions on Electrical Engineering, Electronics, and Communications, 23(2).*  
DOI: [10.37936/ecti-eec.2525232.255314](https://doi.org/10.37936/ecti-eec.2525232.255314)

---

## 👩‍💻 Authors

- **Anya Apavatjrut**  
- **Kanchanarat Chokruay**  
  *Department of Computer Engineering, Chiang Mai University*

GitHub: [Kanchanarat2541](https://github.com/Kanchanarat2541)

---

## 📦 Installation

1. Clone this repository:

git clone https://github.com/Kanchanarat2541/snr-prediction-ml.git
cd snr-prediction-ml

Install dependencies:
pip install -r requirements.txt
Run notebooks in /notebooks/ using Jupyter or Google Colab.


📢 Notes
Data is not publicly shared due to publication constraints.
Code is modular and generalizable for similar regression problems.

📚 Reference Dataset
E. Goldoni et al., "Correlation Between Weather and Signal Strength in LoRaWAN Networks: An Extensive Dataset," Computer Networks, 2022.
DOI: 10.1016/j.comnet.2021.108648


