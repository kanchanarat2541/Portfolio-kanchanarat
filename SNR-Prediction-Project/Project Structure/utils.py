import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_correlation_matrix(df, columns=None, save_path=None):
    if columns:
        df = df[columns]

    plt.figure(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Feature Correlation Matrix")

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Correlation plot saved to {save_path}")
    else:
        plt.show()


def plot_feature_importance(importance_dict, save_path=None):
    keys = list(importance_dict.keys())
    values = list(importance_dict.values())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=values, y=keys)
    plt.xlabel("Importance")
    plt.ylabel("Features")
    plt.title("Feature Importance Summary")

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Feature importance plot saved to {save_path}")
    else:
        plt.show()
