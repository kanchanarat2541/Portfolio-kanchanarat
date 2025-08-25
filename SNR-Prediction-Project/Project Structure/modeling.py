import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor


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


def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    pov = 1 - (np.sum((y_test - predictions) ** 2) / np.sum((y_test - np.mean(y_test)) ** 2))

    return rmse, r2, pov
