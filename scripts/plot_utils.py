import matplotlib.pyplot as plt

def plot_stock_prices(df, stock_symbol, date_column='Date', price_column='Close'):
    """
    Plot the stock's closing prices over time.
    """
    plt.figure(figsize=(12,6))
    plt.plot(df[date_column], df[price_column], label=f"{stock_symbol} Closing Price")
    plt.title(f"{stock_symbol} Stock Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_moving_averages(df, stock_symbol, date_column='Date', price_column='Close', ma_columns=['SMA_50', 'SMA_200']):
    """
    Plot stock price along with moving averages clearly.
    """
    plt.figure(figsize=(12,6))
    plt.plot(df[date_column], df[price_column], label='Close')
    for ma in ma_columns:
        plt.plot(df[date_column], df[ma], label=ma)
    plt.title(f"{stock_symbol} Stock Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_rsi(df, stock_symbol, date_column='Date', rsi_column='RSI_14'):
    """
    Plot the Relative Strength Index (RSI).
    """
    plt.figure(figsize=(12,4))
    plt.plot(df[date_column], df[rsi_column], label='RSI', color='orange')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f"{stock_symbol} Relative Strength Index (RSI)")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_macd(df, stock_symbol, date_column='Date', macd_column='MACD_12_26_9', signal_column='MACDs_12_26_9', hist_column='MACDh_12_26_9'):
    """
    Plot Moving Average Convergence Divergence (MACD).
    """
    plt.figure(figsize=(12,4))
    plt.plot(df[date_column], df[macd_column], label='MACD')
    plt.plot(df[date_column], df[signal_column], label='Signal Line')
    plt.bar(df[date_column], df[hist_column], label='MACD Histogram')
    plt.title(f"{stock_symbol} MACD Indicator")
    plt.xlabel("Date")
    plt.ylabel("MACD Value")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_sentiment_scores(df, date_column='date', sentiment_column='sentiment_score'):
    """
    Plot sentiment scores over time.
    """
    plt.figure(figsize=(12,6))
    plt.plot(df[date_column], df[sentiment_column], marker='o', linestyle='-', label="Sentiment Score")
    plt.title("Sentiment Scores Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sentiment Score")
    plt.grid(True)
    plt.legend()
    plt.show()
