#导入数据集生成工具
from sklearn.datasets import make_blobs
#d导入画图工具
import matplotlib.pyplot as plt
#导入数据集拆分工具
from  sklearn.model_selection import train_test_split
import numpy as np
#生成样本数为200,分类为2，标准差为5的数据集
X,y = make_blobs(n_samples=200,random_state=1,centers=2,cluster_std=5)
#绘制散点图
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.cool,edgecolors='k')

#导入朴素贝叶斯模型
from sklearn.naive_bayes import GaussianNB
#将数据集拆分为训练集和测试集
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=68)
#训练高斯贝叶斯模型
gnb = GaussianNB()
gnb.fit(X_train,y_train)
#获得高斯贝叶斯的分类准确率
predict_proba = gnb.predict_proba(X_test)
#打印结果
print('预测准确率形态:{}'.format(predict_proba.shape))

#打印准确概率的前5个
print(predict_proba[:5])

#设定横轴纵轴范围
x_min,x_max = X[:,0].min()-.5,X[:,0].max()+.5
y_min,y_max = X[:,1].min()-.5,X[:,1].max()+.5
xx,yy = np.meshgrid(np.arange(x_min,x_max,0.2),
#用不同色彩表示不同分类
                np.arange(y_min,y_max,0.2))
Z = gnb.predict_proba(np.c_[xx.ravel(),yy.ravel()])[:,1]
Z = Z.reshape(xx.shape)
#绘制等高线
plt.contourf(xx,yy,Z,cmap= plt.cm.summer,alpha = .8)
#绘制散点图
plt.scatter(X_train[:,0],X_train[:,1],c=y_train,cmap = plt.cm.cool,edgecolors='k')
plt.scatter(X_test[:,0],X_test[:,1],c=y_test,cmap = plt.cm.cool,edgecolors='k',alpha=0.6)
#设置横轴纵轴范围
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
#设置横轴纵轴的单位
plt.xticks(())
plt.yticks(())
#plt.show()

#导入SVC模型
from sklearn.svm import SVC
#使用训练集训练模型
svc = SVC().fit(X_train,y_train)
#获得SVC的决定系数
dec_func = svc.decision_function(X_test)
print(dec_func[:5])

#使用决定系数进行绘图
Z  = svc.decision_function(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
#绘制等高线
plt.contourf(xx,yy,Z,cmap= plt.cm.summer,alpha = .8)
#绘制散点图
plt.scatter(X_train[:,0],X_train[:,1],c=y_train,cmap = plt.cm.cool,edgecolors='k')
plt.scatter(X_test[:,0],X_test[:,1],c=y_test,cmap = plt.cm.cool,edgecolors='k',alpha=0.6)
#设置横轴纵轴范围
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
#设置图题
plt.title('SVC decision_function')

#设置横轴纵轴的单位
plt.xticks(())
plt.yticks(())
plt.show()