import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


iris = load_iris()
#print(iris)


x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)

sklearn.feature_extraction

data = [{'city':'北京','temperature':100},{'city':'上海','temperature':60},{'city':'深圳','temperature':30}]
transfer = sklearn.feature_extraction.DictVectorizer(sparse=False)



new_data = transfer.fit_transform(data)
print(new_data)
print(transfer.get_feature_names())