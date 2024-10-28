from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#导入dendrogram和ward工具
from scipy.cluster.hierarchy import dendrogram,ward
import numpy as np
from sklearn.cluster import DBSCAN

blobs = make_blobs(random_state=1,centers=1)
X_blobs = blobs[0]
plt.scatter(X_blobs[:,0],X_blobs[:,1],c='r',edgecolors='k')
db = DBSCAN()
db_1 = DBSCAN(eps=2)
db_2 = DBSCAN(min_samples=20)


clusters = db.fit_predict(X_blobs)
clusters_1 = db_1.fit_predict(X_blobs)
clusters_2 = db_2.fit_predict(X_blobs)

plt.scatter(X_blobs[:,0],X_blobs[:,1],c=clusters_2,cmap = plt.cm.cool,s=60,edgecolors='k')
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.show()
print('\n\n\n聚类标签:\n{}\n\n\n'.format(clusters))
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_blobs)
x_min,x_max = X_blobs[:,0].min()-0.5,X_blobs[:,0].max ()+0.5
y_min,y_max =X_blobs[:,1].min()-0.5,X_blobs[:,1].max()+0.5
xx,yy = np.meshgrid(np.arange(x_min,x_max,.02),
np.arange(y_min,y_max,.02))
Z = kmeans.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z,interpolation='nearest',
extent=(xx.min(),xx.max(),yy.min(),yy.max()),
cmap=plt.cm.summer,
aspect='auto',origin='lower')
centerorids = kmeans.cluster_centers_
plt.scatter(centerorids[:,0],centerorids[:,1],marker='x',s=150,linewidths=3,color ='b',zorder= 10)
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.yticks(())
plt.show()
#使用连线的方式进行可视化
linkage = ward(X_blobs)
dendrogram(linkage)
ax = plt.gca()
#设定横轴标签
plt.xlabel("Sample index")
plt.ylabel("Cluster distance")
#显示图像
plt.show()