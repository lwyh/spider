from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False # 解决负号不显示问题
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=4202)

rf = RandomForestClassifier(n_estimators=100, random_state=1)
rf.fit(X_train, y_train)
#print(rf)
baseline = rf.score(X_test, y_test)
result = permutation_importance(rf, X_test, y_test, n_repeats=10, random_state=1, scoring='accuracy')

importances = result.importances_mean


plt.bar(range(len(importances)), importances)
plt.xlabel('Feature Index')
plt.ylabel('Permutation Importance')
plt.show()