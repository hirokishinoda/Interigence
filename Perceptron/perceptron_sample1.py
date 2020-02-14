# パーセプトロンのサンプルプログラム
import numpy as np
import pandas as pd
import sklearn.preprocessing as skl # 正規化してくれる

# 乱数の種を設定
#np.random.seed(0)

# トレーニングデータを読み込む
df = pd.read_csv('./fishDataDifficult_train.csv')
df.x1 = skl.scale(df.x1)
df.x2 = skl.scale(df.x2)
num = len(df)

# 各種パラメーターの設定
eta = 0.1
dimention = 3
weight = (np.random.random(dimention) - 0.5)*3

# ここから学習部分
# ランダムにデータをひとつ選んで、内積を計算する
i = np.random.randint(num-1)
data = np.array([1.0, df.x1[i], df.x2[i]])
dot = np.dot(weight, data)

# 正解か不正解か判定
if (dot>0 and df.cls[i]==-1):
    print("不正解")
elif (dot<0 and df.cls[i]==1):
    print("不正解")
else:
    print("正解")
    
