#导入数据集生成器
from sklearn.datasets import make_blobs
#导入KNN分类器
from sklearn.neighbors import KNeighborsClassifier
#导入画图工具
import matplotlib.pyplot as plt
#导入数据集拆分工具
from sklearn.model_selection import train_test_split
#生成样本数为200,分类为2的数据集
data = make_blobs(n_samples=200,centers=2,random_state=8)
X,y=data
#将生成的数据集进行可视化
#plt.scatter(X[:,0],X[:,1],c=y,cmap = plt.cm.spring,edgecolors='k')
#plt.show()
"""
#下面的代码用于画图
x_min,x_max= X[:,0].min() - 1,X[:,0].max() + 1
y_min,y_max = X[:,1].min() -1,X[:,1].max()  + 1
xx,yy = np.meshgrid(np.arange(x_min,x_max,.02),np.arange(y_min,y_max,.02))
Z = clf.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx,yy,Z,cmap=plt.cm.Pastel1)
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.spring,edgecolors='k')
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.title("Classifier:KNN")

#把新的数据点用五行标识出来
#plt.scatter(6.75,4.82,marker = '*',c='red',s=200)
#plt.show()




"""



#生成样本数为500,分类为5的数据集
data2 = make_blobs(n_samples=500,centers=5,random_state=8)
X2,y2=data2
import numpy as np
clf = KNeighborsClassifier()
clf.fit(X2,y2)

x_min,x_max= X2[:,0].min() - 1,X2[:,0].max() + 1
y_min,y_max = X2[:,1].min() -1,X2[:,1].max()  + 1
xx,yy = np.meshgrid(np.arange(x_min,x_max,.02),np.arange(y_min,y_max,.02))
Z = clf.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx,yy,Z,cmap=plt.cm.Pastel1)
plt.scatter(X2[:,0],X2[:,1],c=y2,cmap=plt.cm.spring,edgecolors='k')
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.title("Classifier:KNN")

#将生成的数据集进行可视化
#plt.scatter(X2[:,0],X2[:,1],c=y2,cmap = plt.cm.spring,edgecolors='k')
plt.show()

#将模型的评分进行打印
print('\n\n\n')
print('代码运行结果：')
print('================================================')
print('模型正确率：{:.2f}'.format(clf.score(X2,y2)))
print('================================================')
print('\n\n\n')