#coding:utf-8
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

data2  = ["今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
          "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
"如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

def lets_extract(data):
    transfer = TfidfVectorizer()
    new_data = transfer.fit_transform(data)
    print(new_data.toarray())
    print(transfer.get_feature_names())
    return  None

def fenci_api(t):
    a= jieba.cut(t)
    #传入分词 进行分词
    return  " ".join(list(a))

def  fenci_new(data2):
    data_2 = []
    for st_r in data2:
        i = fenci_api(st_r)
        data_2.append(i)
    return data_2



#文本特征说明
def TFidf(data2):
    n2  = fenci_new(data2)
    lets_extract(n2)
    return  None

TFidf(data2)

