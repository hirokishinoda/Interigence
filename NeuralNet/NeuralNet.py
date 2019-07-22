import numpy as np
from collections import OrdererDict

"""
    Sigmoid
    活性化関数にSigmoid関数を使用したニューロン
"""
class Sigmoid:
    def __init__(self, w, b):
        self.w = w
        self.b = b
        self.eps = 4.0

    def sigmoid(self, x):
        return 1 /(1 + np.exp(-eps*x))

    def forward(self, x):
        y = np.dot(x, self.w) + self.b
        self.out = self.sigmoid(y)
        return self.out

    def backward(self, delta):
        self.delta = 
        return self.delta

class MSE:
    def __init__(self):
        self.eps = 4.0

    def forward(self):
        np.sum()

    def backward(self,y,t):
        self.delta = (y - t) * self.eps * (1 - y) * y
        return self.delta

'''
    3層全結合ネットワーク

'''
class NewralNetwork:
    def __init__(self,inlayer_nodes, hidlayer_nodes, outlayer_nodes):
        # 各層の間の重み
        self.params = {}
        self.params["w1"] = np.random.normal(0, 1.0, (inlayer_nodes, hidlayer_nodes))
        self.params["b1"] = np.random.normal(0, 1.0, (1, hidlayer_nodes))
        self.params["w2"] = np.random.normal(0, 1.0, (hidlayer_nodes, outlayer_nodes))
        self.params["b2"] = np.random.normal(0, 1.0, (1, outlayer_nodes))
        self.params["d1"] = np.zeros((1, outlayer_nodes))
        self.params["d2"] = np.zeros((1, hidlayer_nodes))

        # 各層を構築する
        '''
        point! タプルは参照渡しである!
        '''
        self.layers = OrdererDict()
        self.["layer1"] = Sigmoid(w = self.params["w1"],b = self.params["b1"])
        self.["layer2"] = Sigmoid(w = self.params["w2"],b = self.params["b2"])
        self.lastlayer = MSE()

    # 前向きの計算
    def forward(self,x):
        for layer in self.layers.values():
            x = layer.forward(x)
        return x

    def train(self, x, t):
        # 前向き計算を行う
        y = self.forward(x)
        # 誤差を計算
        self.error = self.lastlayer.forward(y, t)
        print("error : ".format{self.error})

        # BP法
        # 重みの更新量を決定
        delta = self.lastlayer.backward(y, t)
        layers = list(self.layers.values()).reverse
        for layer in layers:
            delta = layer.backward(delta)
        # 重み更新
        self.lastlayer.update(eta = 0.01)
        for layer in layers:
            layer.update(eta = 0.01)
