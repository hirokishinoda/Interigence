import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def error_function(x, params):
    total = 0
    p_x = params.iloc[:,0]
    p_y = params.iloc[:,1]
    for i,_ in enumerate(params):
        total += ((p_x[i] * x[0] + x[1])- p_y[i])**2

    return total/2

# 偏微分を計算
def numerical_diff(f, x, i, params):
    # 丸め誤差で無視されない小さい数
    h = 1e-4

    h_vec = np.zeros_like(x)
    h_vec[i] = h

    return (f(x+h_vec,params) - f(x-h_vec,params)) / (2*h)

# 勾配をまとめる計算
def numerical_gradient(f, x, params):

    grad = np.zeros_like(x)

    for i, _ in enumerate(x):
        grad[i] = numerical_diff(f, x, i, params)

    return grad

# 再急降下法
def gradient_descent(f, initial_position, params, learning_rate=0.001, steps=10000):

    x = initial_position

    for _ in range(steps):
        grad = numerical_gradient(f, x, params)

        x -= learning_rate * grad

    return x

def main(data):
    min_pos = gradient_descent(error_function, [10,7], data)
    print("最小値：{0}".format(min_pos))

if __name__ == "__main__":
    data = pd.read_csv("No1/lsmdata1_train.csv"," ")
    main(data)
