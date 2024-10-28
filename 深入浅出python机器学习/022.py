import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor




fruits = pd.DataFrame({'数值特征':[5,6,7,8,9],'类型特征':['西瓜','香蕉','橘子','苹果','葡萄']})
fruits['数值特征'] =fruits['数值特征'].astype(int)
output = pd.get_dummies(fruits,columns=['数值特征'])
rnd = np.random.RandomState(38)
x = rnd.uniform(-5,5,size = 50)
#向数据中添加噪声
y_no_noise = (np.cos(6*x)+x)
X = x.reshape(-1,1)

y = (y_no_noise+rnd.normal(size=len(x)))/2

line = np.linspace(-5,5,1000,endpoint=False).reshape(-1,1)
mlpr = MLPRegressor().fit(X,y)
knr = KNeighborsRegressor().fit(X,y)
#绘制图像
plt.plot(line,mlpr.predict(line),label='MLP')
plt.plot(line,knr.predict(line),label='KNN')
plt.plot(X,y,'o',c='r')
plt.legend(loc='best')


#装箱处理，离散化处理
bins = np.linspace(-5,5,11)
target_bin = np.digitize(X,bins= bins)
print('装箱数据范围:\n{}'.format(bins))
print('\n前十个数据点的特征值： \n{}'.format(X[:10]))
print('\n前十个数据点所在的箱子:\n{}'.format(target_bin[:10]))

#导入独热编码
from sklearn.preprocessing import OneHotEncoder
onehot = OneHotEncoder()
onehot.fit(target_bin)

X_in_bin = onehot.transform(target_bin)

print('装箱后的数据形态:{}'.format(X_in_bin.shape))
print('\n装箱后的前十个数据点:\n{}'.format(X_in_bin[:10]))

#需要先将稀疏矩阵修改为密集型的Numpy数组
X_in_bin_ex =X_in_bin.toarray()
X_stack = np.hstack((X,X_in_bin_ex))
X_multi = np.hstack((X_in_bin_ex,X*X_in_bin_ex))
print(X_multi.shape)
print(X_multi[0])



# MLP，KNN重新进行回归分析
new_line = onehot.transform(np.digitize(line,bins=bins))
new_line_ex = new_line.toarray()
new_mlpr = MLPRegressor().fit(X_in_bin,y)
new_knr = KNeighborsRegressor().fit(X_in_bin,y)

#重新训练模型
mlpr_multi = MLPRegressor().fit(X_multi,y)
line_multi  = np.hstack([new_line_ex,line*new_line_ex])
#绘制图像
plt.plot(line,mlpr_multi.predict(line_multi),label='MLP Regressor')
for vline in bins:
    plt.plot([vline,vline],[-5,5],':',c='gray')
plt.plot(X,y,'o',c='r')
plt.legend(loc='lower right')
plt.show()



line_stack = np.hstack([line,new_line_ex])
mlpr_interact = MLPRegressor().fit(X_stack,y)
plt.plot(line,mlpr_interact.predict(line_stack),
         label = 'MLP for interaction')
plt.ylim(-4,4)
for vline in bins:
    plt.plot([vline,vline],[-5,5],':',c='k')
plt.legend(loc = 'lower right')
plt.plot(X,y,'o',c='r')
plt.show()
plt.plot(line,new_mlpr.predict(new_line),label='new MLP')
plt.plot(line,new_knr.predict(new_line),label='new KNN')

plt.plot(X,y,'o',c='r')
plt.legend(loc = 'best')
plt.show()


from sklearn.preprocessing import PolynomialFeatures
#向数据集添加多项式
poly =PolynomialFeatures(degree=20,include_bias=False)
X_poly = poly.fit_transform(X)
print(X_poly.shape)
print('原始数据集中在的第一个样本特征:\n{}'.format(X[0]))

print('\n处理后的数据集中在的第一个样本特征:\n{}'.format(X_poly[0]))

print('PolynomialFeature对原始数据处理:\n'.format(poly.get_feature_names_out))


#输入线性回归
from sklearn.linear_model import LinearRegression
#使用处理后的数据训练线性回归模型
LNR_poly = LinearRegression().fit(X_poly,y)
line_poly = poly.transform(line)
#绘制图形
plt.plot(line,LNR_poly.predict(line_poly),label='Linear Regressor')
plt.xlim(np.min(X)-0.5,np.max(X)+0.5)
plt.ylim(np.min(y)-0.5,np.max(y)+0.5)
plt.plot(X,y,'o',c='r')
plt.legend(loc = 'lower right')
plt.show()

#plt.show()
