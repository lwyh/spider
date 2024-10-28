import xgboost as xgb
#python中导入的包名一般不要跟文件名重名
import shap
from  sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

# 导入乳癌数据
breast_cancer = load_breast_cancer()
x = breast_cancer["data"]
y = breast_cancer["target"]

train, test, labels_train, labels_test = train_test_split(x, y, train_size=0.8, random_state=2579)

# 训练一个XGBoost模型
xgb_model = xgb.XGBClassifier(learning_rate=0.1, n_estimators=100)
xgb_model.fit(train, labels_train)

# 对模型文件model进行解释
explainer = shap.TreeExplainer(xgb_model)
# 传入特征矩阵X，计算shap值
shap_values = explainer.shap_values(test)

print("base value:", explainer.expected_value)

# 绘制全局解释图
shap_values_all = explainer.shap_values(test)
shap.summary_plot(shap_values_all, test, plot_type="bar", feature_names=breast_cancer.feature_names)


