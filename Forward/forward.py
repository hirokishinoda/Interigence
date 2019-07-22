import numpy as np

## Newron
class N:
    # 初期化
    # bias : 閾値
    # weight : 重み
    def __init__(self,bias,weight):
        self.bias = bias
        self.weight = weight

    # 活性化関数
    def f(self,x):
        return 0.5 * x

    # 入力の重み付けと総和
    def X(self,x):
        return np.dot(self.weight, x) + self.bias

    # ニューロンの出力
    def result(self,x):
        return self.f( self.X(x) )

# a, b, cのニューロンを作成
b = N(0.4,np.array([0.5,0.1]))
c = N(-0.2,np.array([-0.3,0.6]))
a = N(-0.5,np.array([0.4,0.3]))

# 入力の値
input_x = np.array([1.0,1.0])

# それぞれのニューロンの出力と最終結果
b_r = b.result(input_x)
c_r = c.result(input_x)
a_r = a.result(np.array([b_r, c_r]))
print(b_r," ",c_r," ",a_r," ")
