import xgboost as xgb 
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False # 解决负号不显示问题

# 生成模拟数据集
X, y = make_classification(n_samples=100, n_features=4, n_informative=2, 
                           n_redundant=0, n_clusters_per_class=1, random_state=42)


#使用示例数据集
dtrain = xgb.DMatrix(X,label = y)

# 设置 XGBoost 参数
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'logloss'
}

# 训练 XGBoost 模型
bst = xgb.train(params, dtrain)

# 绘制特征重要性
xgb.plot_importance(bst, importance_type='gain', xlabel='特征重要性', title='XGBoost 特征重要性')
plt.show()