import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import time
#计算距离矩阵
def compute_squared_EDM(X):
    return squareform(pdist(X,metric='euclidean'))

#DBSCAN算法核心过程
def DBSCAN(data,eps,minPts):
    disMat = compute_squared_EDM(data)
    n, m = data.shape
    core_points_index = np.where(np.sum(np.where(disMat <= eps, 1, 0),axis=1 )>=minPts)[0]
    #初始化分类，-1代表未分类
    labels = np.full((n,),-1)
    clusterId = 0
    #遍历所有的核心点
    for pointId in core_points_index:
    #如果核心点未被分类，将其作为的种子类，开始寻找相应簇集
        if(labels[pointId] == -1 ):
            #首先讲点pointedId标记为当前类别(即标识为已操作)
            labels[pointId] = clusterId
            #然后寻找种子点的eps领域且没有被分类的点，将其放入种子集合
            neighbour = np.where((disMat[:,pointId]<= eps)&(labels ==-1))[0]
            seeds = set(neighbour)
            #通过种子点，开始生长，寻找密度可达的数据点,一直到种子集合为空,一个簇集存照完毕
            while len(seeds) > 0:
                #弹出一个新的种子点
                newPoint = seeds.pop()
                #讲newpont标记为当前类
                labels[newPoint] = clusterId
                #寻找newpointed种子点eps领域（包含自己）
                queryResults = np.where(disMat[:,newPoint]<=eps)[0]
                #如果newPoint属于核心点，那么newPoints是可达已扩展的，即密度是可以通过newPoint连续密度可达的
                if len(queryResults) >= minPts:
                    #将领域内且没有被分类的点压入种子集合中
                    for resultPoint in queryResults:
                        if labels[resultPoint] == -1:
                            seeds.add(resultPoint)
            clusterId = clusterId + 1
        return labels
    
#将分类后的数据可视化显示
def plotFeature(data,labels_):
    clusterNum = len(set(labels_))
    fig = plt.figure()
    scatterColors = ['black','blue','green','yellow','red','purple','orange','brown']
    ax = fig.add_subplot(111)
    for i in range(-1,clusterNum):
        colorStyle = scatterColors[i % len(scatterColors)]
        subCluster = data[np.where(labels_ = i)]
        ax.scatter(subCluster[:,0],subCluster[:,1],c=colorStyle,s=12)
    plt.show()

#加载数据
    data = np.loadtxt("D:\\spider\\decode\\cluster.csv",delimiter = ",")
    start = time.clock()
    #DBSCAN聚类并返回标识，E=2，且Minpts=15
    labels = DBSCAN(data,3,30)
    end = time.clock()
    print('finish all in %s' % str(end - start))
    plotFeature(data ,labels)

# -*- coding: utf-8 -*-
import numpy as np
from sklearn.cluster import DBSCAN
# 加载数据
data=np.loadtxt("cluster.csv",delimiter=",")
# 构造一个ϵ=2,MinPts=15的聚类器，距离使用欧式距离
estimator=DBSCAN(eps=2,min_samples=15,metric='euclidean')
# 聚类数据
estimator.fit(data)
# 输出聚类都类别（-1代表异常点）
print(estimator.labels_)



