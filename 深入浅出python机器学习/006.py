from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
#导入数据预处理工具MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
X,y =make_blobs(n_samples=500,centers=5,random_state=8)
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=8)
nb = BernoulliNB()
gnb = GaussianNB()
#使用MinMaxScaler对数据进行预处理，使数据全部为非负值
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
mnb = MultinomialNB()
nb.fit(X_train,y_train)
gnb.fit(X_train,y_train)
mnb.fit(X_train_scaled,y_train)
print('\n\n\n')
print('代码运行结果：')
print('================================================')
print('贝努力贝叶斯模型正确率：{:.3f}'.format(nb.score(X_test,y_test)))
print('高斯贝叶斯模型正确率：{:.3f}'.format(gnb.score(X_test,y_test)))
print('多项式贝叶斯模型正确率：{:.3f}'.format(mnb.score(X_test_scaled,y_test)))
print('================================================')
print('\n\n\n')