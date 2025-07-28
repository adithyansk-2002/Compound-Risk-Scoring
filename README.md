# 🏦 Compound Wallet Risk Scoring

This project analyzes the on-chain behavior of Ethereum wallets and assigns a **risk score (0–1000)** based on historical transaction activity, with a focus on interactions involving **Compound V2/V3 protocols**. It uses data pulled via the **Etherscan API**, extracts key behavioral features, and scores each wallet based on statistical normalization and weighted scoring logic.

---

## 🔍 Objective

The goal is to assess the **risk profile of wallets** by analyzing:
- Transaction frequency and volume
- Success/failure rate of transactions
- Average value transacted

A higher score indicates more stable and trusted behavior, while a lower score indicates irregularities or potential risk.

---

## 📁 Project Structure

```
compound-risk-scoring/
│
├── Wallet id.xlsx              # Wallets to analyze
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── analysis.md                 # Technical justification and logic
│
├── data/                       # Raw transaction data (generated)
│   └── compound_wallet_tx.csv
│
├── output/                     # Final wallet risk scores
│   └── risk_scores.csv
│
└── src/
    ├── fetch_data.py           # Fetch wallet tx data via Etherscan
    ├── features.py             # Feature extraction & normalization
    └── score_model.py          # Risk scoring logic
```

---

## ⚙️ Setup Instructions

### 1. Clone or Download

Download the repo as `.zip`, or:

```bash
git clone https://github.com/adithyansk-2002/compound-risk-scoring.git
cd compound-risk-scoring
```

### 2. Install Dependencies

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate       # Windows
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

## 🔑 Etherscan API Setup

1. Visit [https://etherscan.io/myapikey](https://etherscan.io/myapikey)
2. Create a free account and generate your API key.
3. Open `src/fetch_data.py` and replace this line:

```python
ETHERSCAN_API_KEY = "<YOUR_API_KEY>"
```

---

## 🚀 How to Run

### Step 1: Fetch Transaction Data

```bash
python src/fetch_data.py
```

- Reads wallet addresses from `Wallet id.xlsx`
- Pulls full transaction history via Etherscan
- Saves to: `data/compound_wallet_tx.csv`

### Step 2: Score Wallets

```bash
python src/score_model.py
```

- Extracts transaction-level features
- Normalizes them
- Outputs scores to: `output/risk_scores.csv`

---

## 📊 Features Extracted

| Feature         | Description |
|----------------|-------------|
| total_tx        | Total number of transactions by the wallet |
| total_value     | Total ETH transferred by wallet |
| avg_value       | Average ETH value per transaction |
| failed_tx       | Number of failed transactions |
| success_ratio   | Proportion of successful transactions |

These are normalized (0–1) using **Min-Max scaling**.

---

## 🧮 Scoring Formula

The risk score is a **weighted sum** of normalized features:

```python
score = (
    0.3 * total_tx +
    0.3 * total_value +
    0.2 * success_ratio +
    0.1 * avg_value -
    0.1 * failed_tx
)
```

Then scaled to a range of `0 – 1000` for interpretability.

---

## 📤 Output

After successful execution, your final result will be available at:

```
output/risk_scores.csv
```

Sample:

```
wallet,score
0xabc123...,726
0xdef456...,482
```

