import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./fishDataEasy_train.csv")
print(df.head())

dim = 2
eta = 0.1
W = np.ones(dim+1)

for i in range(df.shape[0]):
    X = np.array([1, df.x1[i], df.x2[i]])

    y = np.dot(W,X.T)

    if y >= 0 and df.cls[i] == -1:
        W = W - eta*X
        print("wrong")
    elif y < 0 and df.cls[i] == 1:
        W = W + eta*X
        print("wrong")
    else:
        print("correct")

print(W)
