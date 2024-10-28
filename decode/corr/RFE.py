from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

#生成模拟数据集
X,y  = make_classification(n_samples=100,n_features=4,n_informative=2,
                           n_redundant=0,n_clusters_per_class=1,random_state=42)
#特征名称
feature_names = ['内功心法强度', '招式复杂度', '使用难度', '对体力的要求']
# 创建随机森林分类器作为选择器的基模型
model = RandomForestClassifier(n_estimators=50, random_state=42)

# RFE模型定义，选择保留2个最重要的特征
rfe = RFE(estimator=model, n_features_to_select=2, step=1)
rfe.fit(X, y)
print(rfe)


# 结果可视化
selected_features = np.array(feature_names)[rfe.support_]
print("被RFE选中的特征是：", selected_features)


#可视化特征的选择情况

plt.figure(figsize=(10, 6))
plt.bar(feature_names, rfe.ranking_, color='skyblue')
plt.title('特征重要性排名（数值越小越重要）')
plt.show()

