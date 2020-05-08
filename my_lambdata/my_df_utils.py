import pandas as pd

def check_null(df):
    return df.isnull().sum()
