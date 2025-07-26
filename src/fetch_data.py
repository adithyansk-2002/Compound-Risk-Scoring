import requests
import pandas as pd
from tqdm import tqdm

ETHERSCAN_API_KEY = "AUF6X8X9UMNQPNXUFQP98541AGHMKDFMCQ"

def fetch_wallet_transactions(wallet):
    url = f"https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": wallet,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": ETHERSCAN_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['result'] if data['status'] == "1" else []

def save_all_wallet_data(excel_file):
    wallet_df = pd.read_excel(excel_file)
    wallets = wallet_df['wallet_id'].tolist()

    all_data = []

    for wallet in tqdm(wallets):
        txs = fetch_wallet_transactions(wallet)
        for tx in txs:
            all_data.append({
                "wallet": wallet,
                "tx_hash": tx['hash'],
                "value": float(tx['value']) / 1e18,
                "from": tx['from'],
                "to": tx['to'],
                "success": tx['isError'] == "0",
                "timestamp": tx['timeStamp']
            })

    df = pd.DataFrame(all_data)
    df.to_csv("data/compound_wallet_tx.csv", index=False)

if __name__ == "__main__":
    save_all_wallet_data("Wallet id.xlsx")
