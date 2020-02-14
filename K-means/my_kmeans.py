# -*- coding: utf-8 -*-
# 2次元プロットデータ（3クラス）のデータを読み込んで，k-means法でクラスタリングする
import numpy as np
import matplotlib.pyplot as plt

# 2点間距離を測る関数
def distance(a, b):
    dist = 0.0
    for i in range(len(a)):
        dist += (a[i] - b[i])**2
    dist = np.sqrt(dist)
    return dist

# データを読み込む
data = np.loadtxt("data.csv", delimiter=",")

# cluster
C = 3
# dimension
D = 2

# クラスタの初期化
Vc = np.zeros(len(data))

# 各データに対してランダムにクラスタを割り振り
for i in range(len(data)):
    Vc[i] = np.random.randint(C)

# データの中からランダムに初期値を決める
#center_gravity = np.zeros((C,D))
#for i in range(C):
#    center_gravity[i] = data[np.random.randint(len(data))]
plt.scatter(data[:,0],data[:,1],c=Vc,marker="o",s=100)
plt.grid()
plt.show()

# クラス分類
for loop in range(100):
    # クラスタの重心を計算
    center_gravity = np.zeros((C,D))
    for i in range(len(data)):
        center_gravity[Vc[i]] += data[i]
    for i in range(C):
        center_gravity[i] /= np.count_nonzero(Vc == i)

    # 距離を計算
    # クラスタを再配置
    for i in range(len(data)):
        min_dist = distance(center_gravity[0],data[i])
        Vc[i] = 0
        for j in range(1,C):
            if distance(center_gravity[j],data[i]) < min_dist:
                min_dist = distance(center_gravity[j],data[i])
                Vc[i] = j

    if loop % 10 == 0:
        plt.scatter(data[:,0],data[:,1],c=Vc,marker="o",s=100)
        plt.scatter(center_gravity[:,0],center_gravity[:,1],marker="x",s=100)
        plt.grid()
        plt.show()
