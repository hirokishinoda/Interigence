# パーセプトロンのサンプルプログラム
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing as skl # 正規化してくれる

# 乱数の種を設定
np.random.seed(0)

# トレーニングデータを読み込む
df = pd.read_csv('./fishDataDifficult_train.csv')
df.x1 = skl.scale(df.x1)
df.x2 = skl.scale(df.x2)
num = len(df)
 
# 各種パラメーターの設定
eta = 0.1
dimention = 3
weight = (np.random.random(dimention) - 0.5)*3

#########################################
# データを無理やり与えて、画面で表示して確認する
#########################################
df.x1[0] = 2
df.x2[0] = 2

df.x1[1] = -2
df.x2[1] = -2

# 1つ目のデータ
i = 0
data = np.array([1.0, df.x1[i], df.x2[i]])
dot = np.dot(weight, data)
print(dot)
# 正解か不正解か判定
if (dot>0 and df.cls[i]==-1):
    print("不正解")
elif (dot<0 and df.cls[i]==1):
    print("不正解")
else:
    print("正解")
    
# 2つ目のデータ
i = 1
data = np.array([1.0, df.x1[i], df.x2[i]])
dot = np.dot(weight, data)
print(dot)
# 正解か不正解か判定
if (dot>0 and df.cls[i]==-1):
    print("不正解")
elif (dot<0 and df.cls[i]==1):
    print("不正解")
else:
    print("正解")
    
# 表示
plt.clf()
#for i in range(len(df)):
for i in range(2):
    if df.cls[i]==1:
        plt.scatter(df.x1[i], df.x2[i], color='r')
    else:
        plt.scatter(df.x1[i], df.x2[i], color='b')

x = np.linspace(-4.0,4.0,100)
y = (-1*weight[1]*x - weight[0])/weight[2]

plt.plot(x,y)

plt.xlim(-4, 4)
plt.ylim(-6.0, 3.0)
plt.grid(True)
plt.show()
    
