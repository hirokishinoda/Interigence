import numpy as np

class N:
    def __init__(self,bias,weight):
        self.bias = bias
        self.weight = weight

    def f(x):
        return 0.5 * x

    def X(x):
        return np.dot(self.weight,x) + self.bias

    def result(x):
        return f(X(x))

x = np.array([0.5,0.05])
w = np.array([0.4,0.3])
bias = -0.5

b = N(0.4,np.array([0.5,0.1]))
c = N(-0.2,np.array([-0.3,0.6]))
a = N(-0.5,np.array([0.4,0.3]))

input_x = np.array([0.0,0.0])

b_r = b.result(input_x)
c_r = c.result(input_x)
a_r = a.result(np.array([b_r, c_r]))

print(b_r," ",c_r," ",a_r," ")

print(result)
