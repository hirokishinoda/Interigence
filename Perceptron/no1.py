import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv("./fishDataEasy_train.csv")
print(data_df.head(5))

print("cls 1")
x1_mean = data_df[data_df['cls'] == 1].x1.mean()
x2_mean = data_df[data_df['cls'] == 1].x2.mean()
x1_std = data_df[data_df['cls'] == 1].x1.std()
x2_std = data_df[data_df['cls'] == 1].x2.std()
print("x1 mean : ",x1_mean)
print("x2 mean : ",x2_mean)
print("x1 std : ",x1_std)
print("x2 std : ",x2_std)

print("cls 2")
x1_mean = data_df[data_df['cls'] == -1].x1.mean()
x2_mean = data_df[data_df['cls'] == -1].x2.mean()
x1_std = data_df[data_df['cls'] == -1].x1.std()
x2_std = data_df[data_df['cls'] == -1].x2.std()
print("x1 mean : ",x1_mean)
print("x1 mean : ",x1_mean)
print("x1 std : ",x1_std)
print("x2 std : ",x2_std)
