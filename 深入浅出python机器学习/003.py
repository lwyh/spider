from sklearn.datasets import load_wine
#从sklearn的datasets模块中加载数据集
wine_dataset = load_wine()

#打印酒数据集中的键
print('\n\n\n')
print('代码运行结果：')
print('================================================')
print("红酒数据集中的键:\n{}".format(wine_dataset.keys()))
print('================================================')
print('\n\n\n')


#打印酒数据集中的特征
print('\n\n\n')
print('代码运行结果：')
print('================================================')
print("红酒数据集中的键:\n{}".format(wine_dataset['data'].shape))
print('================================================')
print('\n\n\n')

print(wine_dataset['DESCR'])

#导入数据集拆分工具
from sklearn.model_selection import train_test_split
#将数据集分为训练数据集和测试数据集
X_train,X_test,y_train,y_test = train_test_split(
    wine_dataset['data'],wine_dataset['target'],random_state=0
)


print('\n\n\n')
print('代码运行结果：')
print('================================================\n')
#打印训练数据集中的特征向量的形态
print('X_train shape:{}'.format(X_train.shape))
#打印测试数据集中的特征向量的形态
print('X_test shape:{}'.format(X_test.shape))
#打印训练数据集中的目标形态
print('y_train shape:{}'.format(y_train.shape))
#打印测试数据集中的目标形态
print('y_test shape:{}'.format(y_test.shape))
print('\n================================================')
print('\n\n\n')
