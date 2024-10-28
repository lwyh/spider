import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer

X,y = make_blobs(n_samples=40,centers=2,random_state=50,cluster_std=2)

X_1 = StandardScaler().fit_transform(X)
X_2 = MinMaxScaler().fit_transform(X)
X_3 = RobustScaler().fit_transform(X)
X_4 = Normalizer().fit_transform(X)
plt.scatter(X_2[:,0],X_2[:,1],c=y,cmap=plt.cm.cool)
plt.scatter(X_3[:,0],X_3[:,1],c=y,cmap=plt.cm.cool)
plt.scatter(X_4[:,0],X_4[:,1],c=y,cmap=plt.cm.cool)
#用散点图的绘制经过预处理的数据点
#plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.cool)
plt.show()