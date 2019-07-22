import numpy as np
import matplotlib.pyplot as plt

def f(a):
    #return (a+1.0)**2 * (a-1.0)**2
    return a**4 - 8*a**3 + 18*a**2 -11

def graphic_f():
    N = 100
    x = np.arange(-1 * N,N)
    y = f(x)

    plt.plot(x,y)
    plt.show()

def gradient(a):
    #return 4*(a**3-a)
    return 4*a**3 - 24*a**2 + 36*a
    #return 3*a**2 - 6*a - 9

def gradient_diff(a_0,eta,step):
    a_k = a_0

    for i in range(step):
        a_k -= eta * gradient(a_k)
        print(a_k)


if __name__ == '__main__':
    # no1
    graphic_f()
    # no2
    #gradient_diff(2.0,0.01)
    #no3
    #gradient_diff(-2.0,0.01)
    #no4
    #gradient_diff(2.0,0.001)
    #no6
    gradient_diff(1.0,0.01,100)
    gradient_diff(5.0,0.01,100)
    #no7

    #no8
