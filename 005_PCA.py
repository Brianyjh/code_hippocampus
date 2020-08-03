#coding:utf-8
#主成分分析
from sklearn.decomposition import PCA

data = [[2,8,4,5], [6,3,0,8], [5,4,9,1]]


def   pca_try(data):

    transfer = PCA(n_components=2)
    new_data = transfer.fit_transform(data)
    print(new_data)
    return  None


pca_try(data)









