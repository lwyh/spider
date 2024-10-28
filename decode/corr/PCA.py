from sklearn.decomposition import PCA 
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

#生成模拟数据集
np.random.seed(42)
X = np.random.rand(100,5)*10

#计算PCA
pca = PCA()
pca.fit(X)

#可视化解释方差比
explained_variance_ratio = pca.explained_variance_ratio_
plt.figure(figsize=(8,6))
plt.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, alpha=0.7, align='center')
plt.xlabel('主成分')
plt.ylabel('解释方差比')
plt.title('主成分解释方差比')
plt.show()

