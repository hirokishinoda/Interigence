# -*- coding: utf-8 -*-
# 2次元プロットデータ（3クラス）のデータを読み込んで，k-means法でクラスタリングする
import numpy as np

# 2点間距離を測る関数
def distance(a, b):
    dist = 0.0
    for i in range(len(a)):
        dist += (a[i] - b[i])**2
    dist = np.sqrt(dist)
    
    return dist


# データを読み込む
data = np.loadtxt("data.csv", delimiter=",")

# データの次元
dim = 2

# クラスターサイズを決定する
NUM = 3

# 各データに対してランダムに各クラスタを割り振る
cluster = []
for i in range(len(data)):
    cluster.append(np.random.randint(NUM))

for time in range(100):
    # 重心を初期化
    center = []
    for i in range(NUM):
        center.append(np.zeros(dim))

    # クラスターの重心を計算する
    for i in range(len(data)):
        center[cluster[i]] += data[i]
    for i in range(NUM):
        center[i] /= cluster.count(i)

    # 各データと各クラスタとの距離を求め，最も近いクラスタに割り当て直す
    for i in range(len(data)):
        dist = distance(center[0], data[i])
        minvalue = dist
        index = 0
        for j in range(1, NUM):
            dist = distance(center[j], data[i])
            if dist<minvalue:
                minvalue = dist
                index = j
        cluster[i] = index

        
# プロットする
import matplotlib.pyplot as plt

for i in range(len(data)):
    if cluster[i]==0:
        plt.scatter(data[i,0], data[i,1], color='r', marker='o', s=20)
    elif cluster[i]==1:
        plt.scatter(data[i,0], data[i,1], color='g', marker='o', s=20)
    else:
        plt.scatter(data[i,0], data[i,1], color='b', marker='o', s=20)
        
# グリッド表示
plt.grid(True)

# 表示
plt.show()
