import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing as skl

# データの読み込み
df = pd.read_csv("./fishDataEasy_train.csv")
# データの正規化
df.x1 = skl.scale(df.x1)
df.x2 = skl.scale(df.x2)

# パラメータ
eta = 0.1
dim = 3
weight = np.random.rand(dim)

# 学習
while True:
    # データの選択
    index = np.random.randint(len(df)-1)
    data = df.values[index,:-1]
    data = np.insert(data, 0, 1.0)
    f = np.dot(weight, data.T)

    # 正解・不正解
    if f >= 0 and df.cls[index] == -1:
        # 不正解 C2をC1と誤った
        weight = weight - eta * data
    if f < 0 and df.cls[index] == 1:
        # 不正解 C1をC2と誤った
        weight = weight + eta * data
    # 正解そのまま

    # 描画
    plt.cla()
    x = np.linspace(-4.0,4.0,100)
    y = (-1*weight[1]*x - weight[0])/weight[2]
    plt.plot(x,y)
    plt.scatter(df.x1,df.x2,c=df.cls,cmap=plt.get_cmap("winter"))

    plt.xlim(-4, 4)
    plt.ylim(-3, 3)
    plt.pause(.1)
