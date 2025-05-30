import pandas as pd

def load_stock_data(filepath, date_column='Date'):
    """
    Load and prepare stock market data from a CSV file.
    Ensures date column is parsed and sorted.
    """
    df = pd.read_csv(filepath, parse_dates=[date_column])
    df.sort_values(by=date_column, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def load_news_data(filepath, date_column='date'):
    """
    Load and prepare financial news data from a CSV file.
    Ensures date column is parsed and sorted.
    """
    df = pd.read_csv(filepath, parse_dates=[date_column])
    df.sort_values(by=date_column, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def merge_datasets(news_df, stock_df, news_date_column='date', stock_date_column='Date'):
    """
    Merge news and stock market dataframes clearly on specified date columns.
    """
    merged_df = pd.merge(
        news_df, 
        stock_df, 
        left_on=news_date_column, 
        right_on=stock_date_column, 
        how='inner'
    )
    merged_df.sort_values(by=stock_date_column, inplace=True)
    merged_df.reset_index(drop=True, inplace=True)
    return merged_df
