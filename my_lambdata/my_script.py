import pandas as pd

# from my_df_utils import check_null, get_confusion_mtx
from my_df_utils import MyUtil

# df = pd.DataFrame({"a": [1,2,3], "b": [4,5,6]})

# print(df.head())

df = pd.DataFrame({"a": [1, None, 3], "b": [4, 5, None], "c": [6, 7, 8], "d": [9, 10, 11]})

y_actu = pd.Series([2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2], name='Actual')
y_pred = pd.Series([0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2], name='Prediction')

print(MyUtil.check_null(df))
print(MyUtil.get_confusion_mtx(y_actu, y_pred))
