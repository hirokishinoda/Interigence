import numpy as np

# 前向きは正しいことを確認済み

class NN:
    """
    初期化
    """
    def __init__(self,in_newrons,mid_newrons,out_newrons):
        np.random.seed(0)
        # 各層のニューロン数
        self.in_newrons = in_newrons
        self.mid_newrons = mid_newrons
        self.out_newrons = out_newrons
        # 各層間の重み行列
        self.W1 = np.array([[0.204113,0.169860],[0.179064,-0.063370]])
        #0.3*np.random.randn(in_newrons, mid_newrons)
        self.W2 = np.array([[0.246988],[-0.181469]])
        #0.3*np.random.randn(mid_newrons, out_newrons)
        self.B1 = np.array([-0.98866,0.160938])
        #0.3*np.random.randn(mid_newrons)
        self.B2 = np.array([-0.133335])
        #0.3*np.random.randn(out_newrons)
        self.eps = 4

    """
    シグモイド関数
    """
    def sigmoid(self,X):
        return 1 / (1 + np.exp(-self.eps * X))

    """
    前向き演算
    """
    def forward(self,X_input):
        # 中間層の出力を計算
        self.O1 = self.sigmoid(np.dot(X_input, self.W1) + self.B1)
        # 最終的な出力値
        self.O2 = self.sigmoid(np.dot(self.O1, self.W2) + self.B2)

    """
    誤差計算
    二乗誤差パターン
    """
    def mean_sqard_error(self, O_out, Y_out):
        return (O_out - Y_out)**2

    """
    BackPropagation
    訓練
    """
    def train(self, X_input, Y_out, eta):
        # 前向き演算
        self.forward(X_input)
        # 誤差を計算
        error = self.mean_sqard_error(self.O2, Y_out)

        # X_inputの形状変更
        # Outの形状を変更
        """
        (1,x_1,x_2,…x_n)^T という形状にする
        """
        X_mat = (np.insert(X_input, 0, 1)).reshape(len(X_input)+1, 1)
        Out_j = (np.insert(self.O1, 0, 1)).reshape(len(self.O1)+1, 1)
        # シグモイドの微分行列作成
        grad_k = (self.eps * (1 - self.O2) * self.O2).reshape(len(self.O2), 1)
        grad_j = (self.eps * (1 - self.O1) * self.O1).reshape(len(self.O1), 1)
        # deltaを先に計算する
        Delta_k = (grad_k * (self.O2 - Y_out).reshape(len(grad_k), 1))
        Delta_j = (grad_j * np.dot(self.W2, Delta_k).reshape(len(grad_j), 1))
        # 重み更新
        dW2 = np.dot(Out_j, Delta_k.reshape(1, len(Delta_k)))
        dW1 = np.dot(X_mat, (grad_j * np.dot(self.W2, Delta_k)).reshape(1, len(Delta_j)))
        self.W2 -= eta * dW2[1:,:]
        self.B2 -= eta * dW2[1,:]
        self.W1 -= eta * dW1[1:,:]
        self.B1 -= eta * dW1[1,:]

        return error

if __name__ == "__main__":
    # 入力，中間，出力層のニューロン数
    input_units, hidden_units, output_units = (2,2,1)
    # データ
    X_train = np.array([[0,0],[0,1],[1,0],[1,1]])
    Y_train = np.array([[0], [1], [1], [0]])
    # エポック数
    epochs = 1000
    # 学習係数
    learning_rate = 0.1

    NN = NN(input_units, hidden_units, output_units)
    NN.forward(X_train)
    print(NN.O2)
    """
    # 学習
    for i in range(epochs):
        total_error = 0
        total_error += NN.train(X_train[0], Y_train[0], learning_rate)
        total_error += NN.train(X_train[1], Y_train[1], learning_rate)
        total_error += NN.train(X_train[2], Y_train[2], learning_rate)
        total_error += NN.train(X_train[3], Y_train[3], learning_rate)
        print("total error = ", total_error/4)

    print(NN.W1)
    print(NN.B1)
    print(NN.W2)
    print(NN.B2)
    # 計算
    for i in X_train:
        NN.forward(i)
        print(i,NN.O2,end="")
        if NN.O2 >= 0.5 : print(" (1.0)")
        else : print(" (0.0)")"""
