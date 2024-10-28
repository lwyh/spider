#导入make_regression数据集生成器
from sklearn.datasets import make_regression
#生成特征数量为1，噪音为50的数据集
X,y = make_regression(n_features=1,n_informative=1,noise=50,random_state=8)
#用散点图将数据进行可视化
#导入画图工具
import matplotlib.pyplot as plt
plt.scatter(X,y,c='orange',edgecolors='k')
#plt.show()

#导入用于回归分析的knn模型
from sklearn.neighbors import KNeighborsRegressor
reg =KNeighborsRegressor(n_neighbors=2)
#用KNN模拟拟合数据
reg.fit(X,y)
#把预测结果用图像进行可视化
import numpy as np
z = np.linspace(-3,3,200).reshape(-1,1)
plt.scatter(X,y,c='orange',edgecolors='k')
plt.plot(z,reg.predict(z),c='k',linewidth =3)
#向图标添加标题
plt.title('KNN Regressor')
plt.show()

#将模型的评分进行打印
print('\n\n\n')
print('代码运行结果：')
print('================================================')
print('模型正确率：{:.2f}'.format(reg.score(X,y)))
print('================================================')
print('\n\n\n')