#导入套索回归模型
from sklearn.linear_model import Lasso
#导入数据集拆分工具
from  sklearn.model_selection import train_test_split
#导入红酒数据集
from sklearn.datasets import load_wine
#导入交叉验证工具
from sklearn.model_selection import cross_val_score
#导入用于分类的支持向量机模型
from sklearn.svm import SVC
#载入红酒数据集
wine  =load_wine()
#将数据集拆分为训练集和测试集
X_train,X_test,y_train,y_test = train_test_split(wine.data,wine.target,random_state=0)
#设置初始分数为0
best_score=0
#设置alpha参数遍历0.01,0.1,1和10
for alpha in [0.01,0.1,1.0,10.0]:
#最大迭代数遍历100，1000，5000，100000
    for max_iter in [100,1000,5000,10000]:
        lasso = Lasso(alpha=alpha,max_iter=max_iter)
#训练套索回归模型
        lasso.fit(X_train,y_train)
        score = lasso.score(X_test,y_test)
#令最佳分数为所有分数中的最高值
        if score> best_score:
            best_score = score
#定义字典，返回最佳参数和最佳最大迭代数
        best_parameters = {'alpha':alpha,'最大迭代次数':max_iter}
#打印结果
print("模型最高分为:{:.3f}".format(best_score))
print("最佳参数设置:{}".format(best_parameters))

#与交叉验证结合的网格搜索
import numpy as np
#alpha参数遍历0.01,0.1,1.0,10
for alpha in [0.01,0.1,1.0,10.0]:
#最大迭代数遍历100，1000，5000，100000
    for max_iter in [100,1000,5000,10000]:
#训练套索回归模型
        lasso = Lasso(alpha=alpha,max_iter=max_iter)
        scores = cross_val_score(lasso,X_train,y_train,cv=6)
        score = np.mean(scores)
        if score >best_score:
            best_score = score
            best_parameters = {'alpha':alpha,'迭代次数':max_iter}

#打印结果
print('模型最高分为:{:.3f}'.format(best_score))
print('最佳参数设置:{}'.format(best_parameters))

#用最佳参数模型拟合数据
lasso = Lasso(alpha=0.01,max_iter= 100).fit(X_train,y_train)
#打印册数数据集得分
print('测试数据集得分:{:.3f}'.format(lasso.score(X_test,y_test)))


#导入网格搜索工具
from sklearn.model_selection import GridSearchCV
#将需要遍历的参数定义为字典
params = {'alpha':[0.01,0.1,1.0,10.0],
          'max_iter':[100,1000,5000,10000]}
#定义网格搜索在使用的模型和参数
grid_search = GridSearchCV(lasso,params,cv = 6)
#使用网格搜索模拟拟合数据
grid_search.fit(X_train,y_train)
#打印结果
print('模型最高分:{:.3f}'.format(grid_search.score(X_test,y_test)))
print('最优参数:{}'.format(grid_search.best_params_))
#打印网格搜索中的best_score属性
print('交叉验证最高分:{:.3f}'.format(grid_search.best_score_))



