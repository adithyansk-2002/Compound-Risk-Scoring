import pandas as pd
from features import extract_features, normalize

def score_wallets(features_df):
    df = normalize(features_df)
    df['score'] = (
        df['total_tx'] * 0.3 +
        df['total_value'] * 0.3 +
        df['success_ratio'] * 0.2 +
        df['avg_value'] * 0.1 -
        df['failed_tx'] * 0.1
    )

    df['score'] = (df['score'] - df['score'].min()) / (df['score'].max() - df['score'].min())
    df['score'] = (df['score'] * 1000).astype(int)
    return df[['wallet', 'score']]

if __name__ == "__main__":
    features_df = extract_features("data/compound_wallet_tx.csv")
    scored_df = score_wallets(features_df)
    scored_df.to_csv("output/risk_scores.csv", index=False)
