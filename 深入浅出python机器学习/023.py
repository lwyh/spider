import pandas as pd
import numpy as np
stock =pd.read_csv('D:\\stock_database\\全部Ａ股20240715.csv',encoding='GBK')
#print(stock.info())
#设置回归分析的目标位涨幅
#删除涨幅列值为'--  '的行
stock = stock[(stock['涨幅%']!='--  ')]
stock = stock.replace('--  ',np.nan)

#stock = stock.drop(columns=['代码','名称','流通市值Z','市值增减','AB股总市值','流通市值','流通股本Z']).astype(float)
#stock = stock.fillna(stock.mean())
stock  = stock.dropna()
print(stock.shape)
#stock = stock.fillna(stock.mean())


df = stock.loc[:,'涨幅%':'流通股(亿)']
corr_matrix = df.corr()
target_corr = corr_matrix['涨幅%']
rank_corr = target_corr.sort_values(ascending=False)
print(rank_corr)



y=stock['涨幅%']
#删除涨幅为'--  '的目标值
y = y.astype(float)

print(y.shape)
#print(y[0])
#提取特征值

features = stock.loc[:,'现价':'流通股(亿)']

features = features.replace('--  ',np.nan)

features = features.astype(float)
features  = features.dropna()
#features = features.fillna(features.mean())
print(features.head())




X = features.values
print(X.shape)
print(X[:1])

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
mlpr = MLPRegressor(random_state=62,hidden_layer_sizes=(100,100),alpha=0.001)
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=62)
#对数据进行预处理
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
#训练神经网络
mlpr.fit(X_train_scaled,y_train)
#打印模型分数
print('模型准确率:{:.2f}'.format(mlpr.score(X_test_scaled,y_test)))


#列出涨幅大于或等于9%的股票
wanted = stock.loc[:,'名称']
print(wanted[y>=10])


#导入特征选择工具
from sklearn.feature_selection import SelectPercentile
#设置特征选择参数
select   = SelectPercentile(percentile=50)
select.fit(X_train_scaled,y_train)
X_train_selected = select.transform(X_train_scaled)

#打印特征选择结果
print('经过缩放的特征形态:{}'.format(X_train_scaled.shape))
print('特征选择后的特征形态:{}'.format(X_train_selected.shape))


#查看哪些特征被保留下来
mask = select.get_support()
print(mask)

#使用图像表示特征选择的结果
import matplotlib.pyplot as plt
plt.matshow(mask.reshape(1,-1),cmap = plt.cm.cool)
plt.xlabel("Feature Selected")
plt.show()

#使用特征选择后的数据集训练神经网络
X_test_selected  = select.transform(X_test_scaled)
mlpr_sp = MLPRegressor(random_state=62,hidden_layer_sizes=(100,100),alpha=0.001)
mlpr_sp.fit(X_train_selected,y_train)
#打印模型分数
print('特征选择后模型得分:{:.2f}'.format(mlpr_sp.score(X_test_selected,y_test)))





#导入基于模型的特征选择工具
from sklearn.feature_selection import SelectFromModel
#导入随机森林模型
from sklearn.ensemble import RandomForestRegressor
#设置模型n_estimators参数
sfm = SelectFromModel(RandomForestRegressor(n_estimators=100,random_state=38),threshold = 'median')
#使用模型拟合数据
sfm.fit(X_train_scaled,y_train)
X_train_sfm = sfm.transform(X_train_scaled)
#打印结果
print('基于随机森林模型进行特征后的数据形态:{}'.format(X_train_sfm.shape))


#显示保留特征
mask_sfm  = sfm.get_support()
print(mask_sfm)

#对特征选择后进行可视化
plt.matshow(mask_sfm.reshape(1,-1),cmap = plt.cm.cool)
plt.xlabel("Features Selected")
plt.show()

#使用模型特征选择后的数据集训练神经网络
x_test_sfm = sfm.transform(X_test_scaled)
mlpr_sfm = MLPRegressor(random_state=62,hidden_layer_sizes=(100,100),alpha=0.001)
mlpr_sfm.fit(X_train_sfm,y_train)
#打印结果
print('随机森林进行特征选择后的模型得分:{:.2f}'.format(mlpr_sfm.score(x_test_sfm,y_test)))


#导入RFE工具
from sklearn.feature_selection import RFE
rfe = RFE(RandomForestRegressor(n_estimators=100,random_state=38),n_features_to_select=12)

#使用RFE工具拟合数据
rfe.fit(X_train_scaled,y_train)
#显示保留的特征

mask = rfe.get_support()
print(mask)

#绘制RFE保留的特征
plt.matshow(mask.reshape(1,-1),cmap = plt.cm.cool)
plt.xlabel("Features Selected")
plt.show()


#使用rfe新的数据集训练神经网络
x_train_rfe = rfe.transform(X_train_scaled)
X_test_rfe = rfe.transform(X_test_scaled)
mlpr_rfe = MLPRegressor(random_state=62,hidden_layer_sizes=(100,100),alpha=0.001)
mlpr_rfe.fit(x_train_rfe,y_train)
#打印模型得分
print("RFE选择特征后模型得分:{:.2f}".format(mlpr_rfe.score(X_test_rfe,y_test)))
