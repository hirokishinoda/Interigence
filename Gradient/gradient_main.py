import numpy as np
import matplotlib.pyplot as plt

def f(a):
    #return (a+1.0)**2 * (a-1.0)**2
    return a**4 - 8 * a**3 + 18 * a**2 -11

def grad_f(a):
    #return 4 * (a**3 - a)
    return 4 * a**3 - 24 * a**2 + 36*a

def graphic_f():
    N = 2
    x = np.arange(-1 * N,N)
    y = f(x)

    plt.plot(x,y)
    plt.show()

def gradient_decent(eta, a_t, step):

    for _ in range(step):
        a_t -= eta * grad_f(a_t)

        print("a = ",a_t)

    return a_t

if __name__ == '__main__':
    graphic_f()
    gradient_decent(0.01, 2.0, 100)
