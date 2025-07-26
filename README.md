# Compound Wallet Risk Scoring

This project scores wallets based on Compound V2/V3 activity using on-chain data.

## Features Used
- Total transactions
- Total value transacted
- Average transaction value
- Transaction success ratio
- Number of failed transactions

## Scoring
Each wallet is scored from 0 to 1000 based on normalized behavior.

## How to Run
1. Add your Etherscan API key in `src/fetch_data.py`
2. Run `fetch_data.py` to get on-chain transactions.
3. Run `score_model.py` to generate scores in `output/risk_scores.csv`.
