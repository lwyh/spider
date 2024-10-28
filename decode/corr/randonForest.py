import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
#用力啊显示中文字体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']

#设置随机种子，已确保示例的可重复性
np.random.seed(42)
#生成模拟数据
data_size = 100
#特征：内力，武器熟练度，轻功，医疗能力
features = np.random.rand(data_size,4)*100
#print(features)
#标签：武力等级，这里假设武功等级由上述特征线性组合加随机噪声得到
labels = (features[:,0]*0.6+features[:,1]*0.2+features[:,2]*0.15+features[:,3]*0.05+np.random.rand(data_size)*50).astype(int)
#print(labels)
#将数据转化成DataFrame，以提高可读性
df = pd.DataFrame(features,columns=['内力','武器熟练度','轻功','医疗能力'])
df['武功等级'] = labels
#使用随机森林分类器
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(df.drop('武功等级',axis=1),df['武功等级'])
#获取特征重要性并排序
importances = model.feature_importances_
#print(importances)
sorted_indices = np.argsort(importances)[::-1]
print(sorted_indices)

#可视化特征重要性
plt.figure(figsize=(10,6))
plt.title("特征重要性：武林高手的武功等级")
plt.bar(range(len(importances)),importances[sorted_indices],color = "skyblue",align = "center")
plt.xticks(range(len(importances)),df.columns[sorted_indices])
plt.show()

