#
# アニメーション
# グラフをアニメーションで表示
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 定義域を入力
xmin = -10.0
xmax = 5.0
num = 100 # 区間内の点の数
x = np.linspace(xmin, xmax, num) # xminからxmaxの区間で，num個のデータを等間隔に生成

# 表示したい関数を設定
def func(x, eps):
    y = 1.0/(1+np.exp(-x*eps))
    return y

def animate(nframe):
    # 定義域から値域を生成
    print(nframe)
    eps = nframe
    y = func(x, eps)
    plt.clf()
    plt.plot(x, y)
    plt.grid()

# main
if __name__ == '__main__':
    fig = plt.figure()
    anim = animation.FuncAnimation(fig, animate, frames=30)
    plt.show()
