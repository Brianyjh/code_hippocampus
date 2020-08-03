#coding:utf-8
#特征降维：对二维数组进行处理，降低特征的个数
#特征之间不相关
#特征选择---- 主成分分析
#过滤式：：：方差选择法   相关系数法（特征与特征之间的相关性与相关程度）
#嵌入式 Embeded

import  pandas as pd
from sklearn.feature_selection import VarianceThreshold

data =  pd.read_csv('factor_returns.csv')
data = data.iloc[:,1:-2]
print(data)
print("---"*100)
print("\n")



#方差过滤
def  variance_new(data):
    transfer = VarianceThreshold(threshold= 18) #阈值
    new_data = transfer.fit_transform(data)
    print(new_data)
    print(new_data.shape)
    return  None

variance_new(data)



