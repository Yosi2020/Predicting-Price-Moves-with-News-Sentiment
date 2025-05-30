# indicator_calculator.py
import pandas as pd
import talib

def calculate_rsi(df, period=14):
    df['RSI'] = talib.RSI(df['Close'], timeperiod=period)
    return df

def calculate_moving_averages(df, short_window=50, long_window=200):
    df[f'MA_{short_window}'] = df['Close'].rolling(window=short_window).mean()
    df[f'MA_{long_window}'] = df['Close'].rolling(window=long_window).mean()
    return df

def calculate_macd(df):
    macd, macdsignal, macdhist = talib.MACD(df['Close'])
    df['MACD'] = macd
    df['MACD_Signal'] = macdsignal
    return df
