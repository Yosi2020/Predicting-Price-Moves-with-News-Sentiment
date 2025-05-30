# plot_utils.py
import matplotlib.pyplot as plt

def plot_stock_prices(df, stock_symbol):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Close'], label=f"{stock_symbol} Closing Price")
    plt.title(f"{stock_symbol} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_sentiment_scores(df):
    plt.figure(figsize=(12,6))
    plt.plot(df['date'], df['sentiment_score'], marker='o', linestyle='-', label="Sentiment Score")
    plt.title("Sentiment Scores Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sentiment Score")
    plt.grid(True)
    plt.legend()
    plt.show()
