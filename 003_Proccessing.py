#coding:utf-8
import sklearn
import  pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data =  pd.read_csv('dating.txt')
print(data)
print("---"*100)
print("\n")
data = data.iloc[:,:3]

#归一化
def  minmax_s(data):
    transfer =  MinMaxScaler()
    new_data = transfer.fit_transform(data)
    print(new_data)
    return  None


minmax_s(data)
print("---"*100)
print("\n")


#标准化
def  std_try(data):
    transfer = StandardScaler()
    new_data = transfer.fit_transform(data)
    print(new_data)
    return None

std_try(data)




