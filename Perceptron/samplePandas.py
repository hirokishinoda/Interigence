import numpy as np
import pandas as pd

# データをpandasのDataFrame形式で読み込む
df = pd.read_csv('fishDataEasy_train.csv')

# 読み込んだDataFrame形式のデータをリストに変換する
a_x1 = list(df[df['cls']==1].x1)
a_x2 = list(df[df['cls']==1].x2)
b_x1 = list(df[df['cls']==-1].x1)
b_x2 = list(df[df['cls']==-1].x2)
