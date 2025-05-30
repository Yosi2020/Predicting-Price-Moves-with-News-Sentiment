import pandas as pd
import pandas_ta as ta

def calculate_rsi(df, period=14, close_column='Close'):
    df[f'RSI_{period}'] = df.ta.rsi(close=close_column, length=period)
    return df

def calculate_moving_averages(df, short_window=50, long_window=200, close_column='Close'):
    df[f'SMA_{short_window}'] = df.ta.sma(close=close_column, length=short_window)
    df[f'SMA_{long_window}'] = df.ta.sma(close=close_column, length=long_window)
    return df

def calculate_macd(df, close_column='Close', fast=12, slow=26, signal=9):
    macd_df = df.ta.macd(close=close_column, fast=fast, slow=slow, signal=signal)
    df = pd.concat([df, macd_df], axis=1)
    return df

def calculate_all_indicators(df, close_column='Close'):
    df = calculate_rsi(df, close_column=close_column)
    df = calculate_moving_averages(df, close_column=close_column)
    df = calculate_macd(df, close_column=close_column)
    return df
