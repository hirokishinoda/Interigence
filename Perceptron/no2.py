import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv("./fishDataEasy_train.csv")
print(data_df.head(5))

x1_mean = data_df.x1.mean()
x2_mean = data_df.x2.mean()
x1_std = data_df.x1.std()
x2_std = data_df.x2.std()
print("x1 mean : ",x1_mean)
print("x1 mean : ",x2_mean)
print("x1 std  : ",x1_std)
print("x1 std  : ",x2_std)

data_df.x1 = (data_df.x1 - x1_mean) / x1_std
data_df.x2 = (data_df.x2 - x2_mean) / x2_std

plt.scatter(data_df.x1, data_df.x2, c=data_df.cls)
plt.show()
