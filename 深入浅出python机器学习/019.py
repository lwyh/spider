from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
scaler  = StandardScaler()
wine = load_wine()
X = wine.data
y = wine.target
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled)
#将三个分类中的主成分提取出来
X0 = X_pca[wine.target==0]
X1 = X_pca[wine.target==1]
X2 = X_pca[wine.target==2]
#绘制散点图
plt.scatter(X0[:,0],X0[:,1],c= 'b',s=60,edgecolors='k')
plt.scatter(X1[:,0],X1[:,1],c= 'g',s=60,edgecolors='k')
plt.scatter(X2[:,0],X2[:,1],c= 'r',s=60,edgecolors='k')

#设置图注
plt.legend(wine.target_names,loc = 'best')
plt.xlabel('component 1')
plt.ylabel('component 2')

#使用主成分绘制热度图
plt.matshow(pca.components_,cmap = 'plasma')
#纵轴为主成分数
plt.yticks([0,1],['component 1','component 2'])
plt.colorbar()

#横轴为原始特征数量
plt.xticks(range(len(wine.feature_names)),wine.feature_names,rotation=60,ha='left')
#显示图像
plt.show()

print(X_pca.shape)
