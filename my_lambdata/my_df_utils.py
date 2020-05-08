import pandas as pd


def check_null(df):
    return df.isnull().sum()


def get_confusion_mtx(y_actu, y_pred):
    """
    #Returns confusion matrix

    #Parameters:
    #   y_actual (pandas series) e.g. y_actual
    #   y_pred (pandas series) e.g. y_pred

    #Returns:
    #   confusion matrix
    """
    return pd.crosstab(y_actu, y_pred)
