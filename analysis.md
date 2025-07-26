## Data Collection
Used Etherscan API to fetch historical transaction data for each wallet.

## Feature Selection
- `total_tx`: High activity indicates usage, potentially lower risk.
- `total_value`: Higher value suggests trust.
- `avg_value`: Avoids spamming.
- `success_ratio`: Failed txs may indicate bot-like or risky behavior.
- `failed_tx`: Penalized.

## Normalization
All features are scaled 0-1 using Min-Max normalization.

## Scoring Logic
Weighted average of features converted to a 0–1000 score.
