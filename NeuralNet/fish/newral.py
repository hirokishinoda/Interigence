import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

"""
3層全結合型ニューラルネットワーク
を作成するクラス
"""
class Newral:
    """
    コンストラクタ
    """
    def __init__(self, in_newrons, mid_newrons, out_newrons):
        # シグモイド関数のepsilon
        self.eps = 4
        # 誤差記録用
        self.errors = np.zeros((1,out_newrons))
        # 中間層用重み
        #self.mid_weight = np.random.random_sample((in_newrons + 1, mid_newrons))
        self.mid_weight = np.array([[-0.133335,-0.098866],
                  [ 0.204113, 0.169860],
                  [-0.063370, 0.179064]])

        # 出力層用重み
        #self.out_weight = np.random.random_sample((mid_newrons + 1, out_newrons))
        self.out_weight = np.array([[0.160938],
                  [0.246988],
                  [-0.181469]])

    """
    シグモイド関数
    ベクトルを計算するために関数をvectorizeで宣言
    """
    def sigmoid(self, vec):
        return np.vectorize(lambda x : 1.0 / (1.0 + np.exp(-1 * self.eps * x)))(vec)

    """
    シグモイド関数の微分関数
    ベクトルを計算するために関数をvectorizeで宣言
    """
    def grad_sigmoid(self, out_vec):
        return np.vectorize(lambda x : self.eps * (1 - x) * x)(out_vec)

    """
    2乗和誤差
    """
    def mean_sqard_error(self, out_vec, t_vec):
        return np.vectorize(lambda x,y : (x - y)**2)(out_vec, t_vec)

    """
    前向きの計算

    行列で書き下すと分かるはず…
    仮想ニューロンを導入しているので(1,x_1,x_2...)^Tと
    の掛け算になる．
    """
    def forward(self, x):
        # 中間層の出力
        out_mid = self.sigmoid(np.r_[np.array([1]), x].dot(self.mid_weight))
        # 出力層の出力
        out_out = self.sigmoid(np.r_[np.array([1]), out_mid].dot(self.out_weight))

        return (out_mid, out_out)

    def predict(self, x, t):
        right = 0

        for i,j in zip(x,t):
            mid,out = self.forward(i)
            print(i,j)
            if out >= 0.5 : ans = 1
            else : ans = 0
            print(out,ans)

            if ans == j : right += 1

        return right / len(t)
    """
    学習を行う
    """
    def train(self, x, t, eta, times):
        for i in range(times):
            # 誤差の合計値
            total_error = 0
            # 全パターン学習
            for j, k in zip(x, t):
                total_error += N.BP(j, k, eta)
            # 誤差を記録
            print("error : ",total_error)
            self.errors = np.append(self.errors, total_error.reshape(1,-1), axis=0)

    """ 1パターン分の学習を行う """
    def BP(self, x, t, eta):
        # 前向きの計算
        out_mid, out_out = self.forward(x)
        # 誤差の計算
        error = self.mean_sqard_error(out_out, t)
        # デルタを先に計算する
        out_delta = (out_out - t) * self.grad_sigmoid(out_out)
        mid_delta = self.grad_sigmoid(out_mid) * (self.out_weight[1:,:].dot(out_delta))
        # 更新量を計算
        update_out = np.r_[np.array([1]), out_mid].reshape(-1,1).dot(out_delta.reshape(1,-1))
        update_mid = np.r_[np.array([1]), x].reshape(-1,1).dot(mid_delta.reshape(1,-1))
        # 更新
        self.out_weight -= eta * update_out
        self.mid_weight -= eta * update_mid

        return error

    """
    誤差の変化を確認するグラフ
    """
    def error_graph(self):
        #plt.figure(figsize=(10,20))
        plt.xlabel("ephocs")
        plt.ylabel("error")
        plt.plot(self.errors[:,0],"r--")
        plt.show()
        #plt.savefig("../report/img/error2.pdf")

def make_dataset():
    # ファイル読込
    x_A = pd.read_csv("../data/fishA.train", sep='\s+', header=None).values
    x_B = pd.read_csv("../data/fishB.train", sep='\s+', header=None).values
    # 入力と出力を結合
    xy_A = np.insert(x_A, 2, 1,axis=1) # Aは教師1
    xy_B = np.insert(x_B, 2, 0,axis=1) # Bは教師0
    xy = np.vstack((xy_A,xy_B)) # 結合
    # シャッフル
    index = list(range(xy.shape[0]))
    random.shuffle(index)
    dataset = xy[index]
    print("data set\n",dataset[:10])
    # テストとトレインに分ける
    train, test = np.split(dataset, [int(dataset.shape[0] * 0.9)])

    return (train, test)

if __name__ == "__main__":
    # 各層のニューロン数
    in_newrons, mid_newrons, out_newrons = (2, 2, 1)
    # データセット作成
    train,test = make_dataset()
    # 入力
    x = train[:,:-1]
    # 出力
    t = train[:,-1]

    # ニューラルネット
    N = Newral(in_newrons, mid_newrons, out_newrons)
    # 訓練
    N.train(x, t, eta = 0.1, times = 1000)
    # 誤差グラフ
    N.error_graph()

    # 前向き計算で確認
    rate = N.predict(test[:,:-1],test[:,-1])
    print(rate)
