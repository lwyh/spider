from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
X,y = make_blobs(n_samples=200,centers=2,cluster_std=5)
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=38)
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
print('\n\n\n')
print('代码运行结果')
print('===================')
print('训练集数据形态:',X_train_scaled.shape,
      '\n测试数据集形态:', X_test_scaled.shape)
print('\n=========================')
print('\n\n\n')

plt.scatter(X_train[:,0],X_train[:,1])
plt.scatter(X_train_scaled[:,0],X_train_scaled[:,1],marker='^',
            edgecolors='k')
plt.title('trianing set & scaled training set')
plt.show()

from sklearn.model_selection import GridSearchCV
params ={'hidden_layer_sizes':[(50,),(100,),(100,100)],
         'alpha':[0.0001,0.001,0.01,0.1]}
grid = GridSearchCV(MLPClassifier(max_iter=1600,random_state=38),param_grid=params,cv=3)
grid.fit(X_train_scaled,y_train)
print('\n\n\n')
print('代码运行结果: ')
print('================================\n')
print('模型最佳参数{:.2f}'.format(grid.best_score_))
print('模型最佳参数:{}'.format(grid.best_params_))
print('测试集得分:{}'.format(grid.score(X_test_scaled,y_test)))
print('\n\n\n')






from sklearn.pipeline import Pipeline
pipline = Pipeline([('scaler',StandardScaler()),
          ('mlp',MLPClassifier(max_iter=1600,random_state=38))])
pipline.fit(X_train,y_train)
print('使用管道模型的MLP模型评分:{:.2f}'.format(
    pipline.score(X_test,y_test)
))

params ={'mlp__hidden_layer_sizes':[(50,),(100,),(100,100)],
         'mlp__alpha':[0.0001,0.001,0.01,0.1]}
grid = GridSearchCV(pipline,param_grid=params,cv =3)
grid.fit(X_train,y_train)
print('\n\n\n')
print('代码运行结果')
print('=========================\n')
print('交叉验证最高分:{:.2f}'.format(grid.best_score_))
print('模型最优参数:{}'.format(grid.best_params_))
print('测试得分:{}'.format(grid.score(X_test,y_test)))
print('\n============================')
print('\n\n\n')
