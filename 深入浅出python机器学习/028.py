import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
#导入特征选择模块
from sklearn.feature_selection import SelectFromModel
#导入随机森林模型
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
stock =pd.read_csv('D:\\stock_database\\深证Ａ股20240717.csv',encoding='GBK')
stock = stock.loc[:,'涨幅%':'流通股(亿)']
stock = stock.replace('--  ',np.nan)
#df = df.dropna()
stock = stock.fillna(0)
print(stock.head())
"""
df = stock.loc[:,'涨幅%':'流通股(亿)']
df = df.replace('--  ',np.nan)
#df = df.dropna()
df = df.fillna('0')
corr_matrix = df.corr()
target_corr = corr_matrix['涨幅%']
rank_corr = target_corr.sort_values(ascending=False)
print(rank_corr)
"""
#定义数据集中的特征X,y
X = stock.loc[:,'现价':'流通股(亿)'].values
y = stock['涨幅%']

#导入交叉验证
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPRegressor
#使用交叉验证对MLP模型进行评分
scores = cross_val_score(MLPRegressor(random_state=38),X,y,cv=3)


#建立包含预处理和mlp模型的管道模型
#导入make_pipline模块
from sklearn.pipeline import make_pipeline
#对比两张方法的语法
pipeline  = Pipeline([('scaler',StandardScaler()),('mlp',MLPRegressor(random_state=38))])

pipe = make_pipeline(StandardScaler(),MLPRegressor(random_state=38))
#print(pipeline.steps)
#print('\n',pipe.steps)

#进行交叉验证
scores = cross_val_score(pipe,X,y,cv=3)

#向管道模型添加特征选择步骤
#建立管道模型
pipe = make_pipeline(StandardScaler(),
              SelectFromModel(RandomForestRegressor(random_state=38)),
              MLPRegressor(random_state=38))
#print(pipe.steps)

#交叉验证再次进行评分
scores  = cross_val_score(pipe,X,y,cv=3)


#使用管道模型拟合数据
pipe.fit(X,y)
#查询哪些特征被选择
mask =pipe.named_steps['selectfrommodel'].get_support()
#print(mask)


#管道中MLP模型和随即森林模型对比
#定义参数字典
params = [{'reg':[MLPRegressor(random_state=38)],'scaler':[StandardScaler(),None]},
          {'reg':[RandomForestRegressor(random_state=38)],'scaler':[None]}]
#下面对pipeline进行实例化
pipe = Pipeline([('scaler',StandardScaler()),('reg',MLPRegressor())])
#对管道模型进行网格搜索
grid  = GridSearchCV(pipe,params,cv=3)
grid.fit(X,y)





#使用管道模型寻找最优参数(将网格搜索放入管道模型中)
#在参数字典中增加MLP隐藏层和随机森林中estimator数量的选项

params = [{'reg':[MLPRegressor(random_state=38,max_iter=1000)],'scaler':[StandardScaler(),None],
  'reg__hidden_layer_sizes':[(50,),(100,),(100,100)]},
          {'reg':[RandomForestRegressor(random_state=38)],'scaler':[None],
           'reg__n_estimators':[100,500,1000]}]
#建立管道模型
pipe = Pipeline([('scaler',StandardScaler()),('reg',MLPRegressor())])
#建立网格搜索
grid = GridSearchCV(pipe,params,cv=3)
grid.fit(X,y)











print('\n\n\n')
print('代码运行结果')
print('============================\n')
print(X.shape,y.shape)
print('模型平均分:{:.2f}'.format(scores.mean()))
print('最佳模型:{}'.format(grid.best_params_))
print('\n模型最佳得分是:{:.2f}'.format(grid.best_score_))
print('\n=================================')
print('\n\n\n')
