import numpy as np
import matplotlib.pyplot as plt

def f(a):
    return (a+1.0)**2 * (a-1.0)**2

def graphic_f():
    N = 2
    x = np.arange(-1 * N,N)
    y = f(x)

    plt.plot(x,y)
    plt.show()


if __name__ == '__main__':
    graphic_f()
