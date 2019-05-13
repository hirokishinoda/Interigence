import numpy as np
from matplotlib import pyplot as plt

def error_function(x):
    return x[0] ** 2 + x[1] ** 2

# 偏微分を計算
def numerical_diff(f, x, i):
    # 丸め誤差で無視されない小さい数
    h = 1e-4
    
    h_vec = np.zeros_like(x)
    h_vec[i] = h

    return (f(x+h_vec) - f(x-h_vec)) / (2*h)

# 勾配をまとめる計算
def numerical_gradient(f, x):

    grad = np.zeros_like(x)

    for i, _ in enumerate(x):
        grad[i] = numerical_diff(f, x, i)

    return grad

# 再急降下法
def gradient_descent(f, initial_position, learning_rate=0.1, steps=100):
    
    x = initial_position

    for _ in range(steps):
        grad = numerical_gradient(f, x)

        x -= learning_rate * grad

    return x

def main():
    min_pos = gradient_descent(error_function, [1,2])
    print("最小値：{0}".format(min_pos))

if __name__ == "__main__":
    main()
