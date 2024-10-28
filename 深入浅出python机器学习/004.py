import numpy as np

#将X,yf赋值为np数组
X = np.array([[0,1,0,1],
              [1,1,1,0],
              [0,1,1,0],
              [0,0,0,1],
              [0,1,1,0],
              [0,1,0,1],
              [1,0,0,1]])
y=np.array([0,1,1,0,1,0,0])
#对于不同分类在计算每个特征为1的额数量
counts ={}
for label in np.unique(y):
    counts[label] = X[y==label].sum(axis=0)
#打印计数结果
print("feature counts:\n{}".format(counts))
