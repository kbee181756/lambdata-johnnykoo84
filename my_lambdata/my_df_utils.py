import pandas as pd

class MyUtil:

    def __init__(self):
        pass

    def check_null(df):
        return df.isnull().sum()

    def get_confusion_mtx(y_actu, y_pred):
        """
        #Returns confusion matrix from pd Series

        #Parameters:
        #   y_actual (pandas series) e.g. y_actual
        #   y_pred (pandas series) e.g. y_pred

        #Returns:
        #   confusion matrix
        """

        return pd.crosstab(y_actu, y_pred)
