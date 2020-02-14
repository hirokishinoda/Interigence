# 2次元(2クラス) 
# 表示
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# データ読み込み
df = pd.read_csv('fishDataEasy_train.csv')

# 散布図をプロットする
for i in range(len(df)):
      if df.cls[i]==1:
            plt.scatter(df.x1[i],df.x2[i], color='r',marker='o', s=30)
      else:
            plt.scatter(df.x1[i],df.x2[i], color='b',marker='x', s=30)

# 表示
plt.grid(True)

# 表示
plt.show()
