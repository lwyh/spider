from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False # 解决负号不显示问题

# 使用示例数据集
X, y = make_classification(n_samples=100, n_features=4, n_informative=2, 
                           n_redundant=0, n_clusters_per_class=1, random_state=4202)


print(X.shape)
# 加载示例数据集
X, y = load_breast_cancer(return_X_y=True)

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# 训练一个随机森林模型
rf = RandomForestClassifier(n_estimators=100, random_state=1)
rf.fit(X_train, y_train)

# 获取测试数据上的基准准确率
base_acc = accuracy_score(y_test, rf.predict(X_test))

# 初始化一个空列表来存储特征重要性
importances = []

# 遍历所有特征，并逐个移除特征后重新训练模型，计算准确率变化
for i in range(X_train.shape[1]):
    X_temp = np.delete(X_train, i, axis=1)  # 移除一个特征
    rf.fit(X_temp, y_train)  # 重新训练模型
    acc = accuracy_score(y_test, rf.predict(np.delete(X_test, i, axis=1)))  # 计算测试准确率
    importances.append(base_acc - acc)  # 计算特征重要性，即准确率变化量

# 绘制特征重要性柱状图
plt.figure(figsize=(10, 6))
plt.bar(range(len(importances)), importances, color='skyblue')
plt.xlabel('特征编号')
plt.ylabel('准确率变化量')
plt.title('Leave-one-out 特征重要性分析')
plt.xticks(range(len(importances)), range(1, len(importances) + 1))
plt.show()