# data_loader.py
import pandas as pd

def load_news_data(filepath):
    return pd.read_csv(filepath)

def load_stock_data(filepath):
    return pd.read_csv(filepath, parse_dates=['Date'])

def merge_datasets(news_df, stock_df):
    merged_df = pd.merge(news_df, stock_df, left_on='date', right_on='Date', how='inner')
    return merged_df
