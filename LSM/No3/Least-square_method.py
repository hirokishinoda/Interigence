import numpy as np
import pandas as pd

# 最小二乗法の正規方程式を関数化
# data_x : 入力データ
# data_y : 出力データ
# Dim    : 求める方程式の次数
def Least_square(data_x,data_y,Dim):
    DataLength = len(data_x)
    # 入力データ
    # X : 入力データ列ベクトル
    # Y : 出力データ列ベクトル
    X = data_x
    Y = data_y
    print("--Input Data--")
    print(X,Y)

    # 係数行列のリスト作成
    tmp_list = []
    matrix_length = Dim+1

    for i in range(matrix_length):
        for j in range(matrix_length):
            tmp_list.append( np.sum((X**(2*Dim - (i+j)))) )

    # 行列形式に変換
    matrix = np.array(tmp_list).reshape((matrix_length, matrix_length))
    print("--Coefficient Matrix--")
    print(matrix)

    # 逆行列を計算
    matrix_inv = np.linalg.inv(matrix)
    print("--Inverse Matrix--")
    print(matrix_inv)

    # Yに関する列
    tmp_list = []
    for k in range(matrix_length):
            tmp_list.append( np.sum(X**(Dim-k)) )
    Column_vec = np.array(tmp_list)
    print("--Column Vector--")
    print(Column_vec)

    # 係数の算出
    A = np.dot(matrix_inv, Column_vec)
    print("--Answer--")
    print(A)

    return A

train_df = pd.read_csv("./lsmdata3_train.csv"," ")
test_df = pd.read_csv("./lsmdata3_test.csv"," ")
print(train_df.head)
Least_square(train_df.iloc[:,0],train_df.iloc[:,1],3)
