from sklearn.datasets import load_wine
import numpy as np
from sklearn import svm 
import matplotlib.pyplot as plt

def make_meshgrid(x,y,h =.02):
    x_min,x_max = x.min()-1,x.max()+1
    y_min,y_max = y.min()-1,y.max()+1
    xx,yy = np.meshgrid(np.arange(x_min,x_max,h),
                        np.arange(y_min,y_max,h))
    return xx,yy

#定义一个绘制等高线的函数
def plot_contours(ax,clf,xx,yy,**params):
    Z = clf.predict(np.c_[xx.ravel(),yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx,yy,Z,**params)
    return out

#使用酒的数据集
wine = load_wine()
# 选取数据集的前两个特征
X = wine.data[:,:2]
y = wine.target
C = 1.0 #SVM的正则化参数
"""
models = (svm.SVC(kernel='linear',C = C),svm.LinearSVC(C=C),
          svm.SVC(kernel='rbf',gamma=0.7,C = C),
          svm.SVC(kernel='poly',gamma=0.7,C = C))


"""
models = (svm.SVC(kernel='rbf',gamma=0.7,C = C),
          svm.SVC(kernel='rbf',gamma=1,C = C),
          svm.SVC(kernel='rbf',gamma=10,C = C))

models = (clf.fit(X,y) for clf in models)


#设定标题
titles = ('gamma = 0.1',
          'gamma = 1',
          'gamma = 10')


#设定一个子图像的个数和排列方式
#fig,sub = plt.subplots(2,2)
fig,sub = plt.subplots(1,3,figsize=(10,3))

#plt.subplots_adjust(wspace=0.4,hspace=0.4)

#使用前面定义的函数进行画图
X0,X1 = X[:,0],X[:,1]
xx,yy=make_meshgrid(X0,X1)

for clf,title,ax in zip(models,titles,sub.flatten()):
    plot_contours(ax,clf,xx,yy,cmap=plt.cm.plasma,alpha = 0.8)
    ax.scatter(X0,X1,c=y,cmap=plt.cm.plasma,s=20,edgecolors='k')
    ax.set_xlim(xx.min(),xx.max())
    ax.set_ylim(yy.min(),yy.max())
    ax.set_xlabel('Feature 0')
    ax.set_ylabel('Feature 1')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)
#将图形显示出来
plt.show()