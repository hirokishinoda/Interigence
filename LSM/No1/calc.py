import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

def n_function(val,params):
    return val * params[0] + params[1]

def calc_model_output(data_x,params):
    answer = []

    for val_x in data_x:
        tmp_ans = n_function(val_x,params)
        answer.append(tmp_ans)

    return answer

test_df = pd.read_csv("./lsmdata1_test.csv"," ")
data_x = test_df.iloc[:,0]
data_y = test_df.iloc[:,1]
params = [1.826452,3.570658]

print(data_x)

model_y = calc_model_output(data_x,params)
print("--test data--")
print(model_y)
print("--test RMSE--")
print(np.sqrt(mean_squared_error(data_y,model_y)))

test_df = pd.read_csv("./lsmdata1_train.csv"," ")
data_x = test_df.iloc[:,0]
data_y = test_df.iloc[:,1]

model_y = calc_model_output(data_x,params)
print("--train data--")
print(model_y)
print("--train RMSE--")
print(np.sqrt(mean_squared_error(data_y,model_y)))
