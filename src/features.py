import pandas as pd
import numpy as np

def extract_features(file_path):
    df = pd.read_csv(file_path)

    features = []

    for wallet, group in df.groupby("wallet"):
        total_tx = len(group)
        total_value = group['value'].sum()
        avg_value = group['value'].mean()
        failed_tx = (~group['success']).sum()
        success_ratio = group['success'].mean()

        features.append({
            "wallet": wallet,
            "total_tx": total_tx,
            "total_value": total_value,
            "avg_value": avg_value,
            "failed_tx": failed_tx,
            "success_ratio": success_ratio
        })

    return pd.DataFrame(features)

def normalize(df):
    df_norm = df.copy()
    for col in df.columns:
        if col != "wallet":
            df_norm[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df_norm
