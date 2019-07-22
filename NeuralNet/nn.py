import numpy as np

class NN:
    def __init__(self,in_newrons,mid_newrons,out_newrons):
        # 各層のニューロン数
        self.in_newrons = in_newrons
        self.mid_newrons = mid_newrons
        self.out_newrons = out_newrons
        # 各層間の重み行列
        self.W1 = np.random.randn(in_newrons, mid_newrons)
        self.W2 = np.random.randn(mid_newrons, out_newrons)
        self.B1 = np.random.randn(mid_newrons)
        self.B2 = np.random.randn(out_newrons)

    def sigmoid(self,X):
        return 1 / (1 + np.exp(-X))

    """
    前向き演算
    """
    def forward(self,X_input):
        Y1 = self.sigmoid( np.dot(X_input, W1) + B1 )
        Y2 = self.sigmoid( np.dot(Y1, W2) + B2 )

        return Y2

    """
    誤差計算
    二乗誤差パターン
    """
    def mean_sqard_error(O_out,Y_out):
        return (O_out - Y_out)**2

    """
    BackPropagation
    """
    def train(self, X_input, Y_out, eta):
        # 前向き演算
        Out = self.forward(X_input)
        # 誤差を計算
        error = self.mean_sqard_error(Out, Y_out)
        print("[Error] -- ", error)
        # deltaを先に計算する
        Delta_k = (grad_k * (Out - Y_out))
        Delta_j = np.dot((grad_j * self.W2), Delta_k)
        # 重み更新
        self.W1 -= eta * np.dot(Out_j, Delta_k.T)
        self.W2 -= eta * np.dot(Out_i, Delta_j.T)

        return error

if __name__ == "__main__":
    input_units, hidden_units, output_units = (2,2,1)

    X_train = np.array([[0,0],[0,1],[1,0],[1,1]])
    Y_train = np.array([[0], [1], [1], [0]])

    epochs = 3000

    learning_rate = 0.01

    NN = NN(input_units, hidden_units, output_units)
    for i in range(epochs):
        NN.train(X_train, Y_train, learning_rate)
