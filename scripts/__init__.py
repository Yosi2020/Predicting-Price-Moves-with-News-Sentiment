# Inside your notebook
import sys
sys.path.append('../')  # Ensure your scripts folder is in the path.

from scripts import (
    load_news_data,
    load_stock_data,
    merge_datasets,
    plot_stock_prices,
    plot_sentiment_scores,
    calculate_rsi,
    calculate_moving_averages,
    calculate_macd,
    apply_sentiment_analysis
)
