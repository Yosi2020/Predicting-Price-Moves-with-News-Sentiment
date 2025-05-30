# 📂 Scripts Folder

This directory contains Python scripts organized to simplify, modularize, and streamline your data analysis workflow for stock market analytics and sentiment analysis.

---

## 📝 Script Descriptions

| Script                      | Description                                                                 |
| --------------------------- | --------------------------------------------------------------------------- |
| **data_loader.py**          | Loads and prepares CSV datasets (stock and news data).                      |
| **indicator_calculator.py** | Computes financial indicators (SMA, RSI, MACD) clearly using `pandas-ta`.   |
| **sentiment_utils.py**      | Performs sentiment analysis on text data using TextBlob.                    |
| **plot_utils.py**           | Provides reusable plotting functions (stock prices, indicators, sentiment). |
| \***\*init**.py\*\*         | Enables simpler imports from the scripts folder.                            |

---

## 🚀 How to Use These Scripts

Below are quick examples of how you can clearly use each of these scripts:

### ✅ **Load Stock Data**

````python
from scripts import load_stock_data

df = load_stock_data('AAPL.csv')
print(df.head())

### ✅ **Calculate Indicators**

```python
from scripts import calculate_all_indicators

df = calculate_all_indicators(df)
print(df.head())
````

### ✅ **Perform Sentiment Analysis**

```python
from scripts import apply_sentiment_analysis

df = apply_sentiment_analysis(df, text_column='headline')
print(df.head())
```

### ✅ **Plot Stock Prices**

```python
from scripts import plot_stock_prices

plot_stock_prices(df, stock_symbol='AAPL')
plot_moving_averages(df, short_window=50, long_window=200)
plot_rsi(df, rsi_period=14)
plot_macd(df, macd_short=12, macd_long=26, macd_signal=9)
```

### ✅ **Plot Sentiment Analysis**

```python
from scripts import plot_sentiment_scores

plot_sentiment_scores(df)
```

### ✅ **Recommended Folder Structure**

scripts/
├── data_loader.py
├── indicator_calculator.py
├── sentiment_utils.py
├── plot_utils.py
├── **init**.py
└── README.md

---

### ⚙️ Installation Requirements

```bash
pip install pandas matplotlib pandas-ta textblob
```
