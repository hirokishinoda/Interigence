import numpy as np
import matplotlib.pyplot as plt

class Newral:
    def __init__(self, in_newrons, mid_newrons, out_newrons):
        self.eps = 4
        self.errors = np.zeros((1,out_newrons))
        self.mid_weight = np.array([[-0.133335,-0.098866],
                                    [ 0.204113, 0.169860],
                                    [-0.063370, 0.179064]])
        #np.random.random_sample((in_newrons + 1, mid_newrons))
        self.out_weight = np.array([[0.160938],
                                    [0.246988],
                                    [-0.181469]])
        #np.random.random_sample((mid_newrons + 1, out_newrons))

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

    def mean_sqard_error(self, out_vec, t_vec):
        return np.vectorize(lambda x,y : (x - y)**2)(out_vec, t_vec)

    """
    前向きの計算

    行列で書き下すと分かるはず…
    仮想ニューロンを導入しているので(1,x_1,x_2...)^Tと
    の掛け算になる．
    """
    def forward(self, x):
        out_mid = self.sigmoid(np.r_[np.array([1]), x].dot(self.mid_weight))
        out_out = self.sigmoid(np.r_[np.array([1]), out_mid].dot(self.out_weight))

        return (out_mid, out_out)

    """
    学習を行う
    """
    def train(self, x, t, eta, times):
        for i in range(times):
            total_error = 0
            for j, k in zip(x, t):
                total_error += N.BP(j, k, eta)
            self.errors = np.append(self.errors, total_error.reshape(1,-1), axis=0)

    # 1パターン分の学習を行う
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

if __name__ == "__main__":
    # 各層のニューロン数
    in_newrons, mid_newrons, out_newrons = (2, 2, 1)
    # 入力
    x = np.array([[0,0],[0,1],[1,0],[1,1]])
    # 出力
    t = np.array([[0],[1],[1],[0]])

    # ニューラルネット
    N = Newral(in_newrons, mid_newrons, out_newrons)
    # 訓練
    N.train(x, t, eta = 0.1, times = 1000)
    # 誤差グラフ
    N.error_graph()

    # 前向き計算で確認
    for i,j in zip(x,t):
        o1,o2 = N.forward(i)
        print(i,o2,j)
