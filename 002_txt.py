#coding:utf-8

import sklearn
from sklearn.datasets import load_iris
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# txt Feature Extraction

data = ["蓝蓝的 天空银河 里","有只 小白船"]


transfer = CountVectorizer()
new_data = transfer.fit_transform(data)
print(new_data.toarray())
print(transfer.get_feature_names())