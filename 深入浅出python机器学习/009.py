from sklearn.ensemble import RandomForestClassifier
from sklearn import tree,datasets
from sklearn.model_selection import train_test_split
#载入红酒数据集
wine = datasets.load_wine()
#选择数据集前两个特征
X = wine.data[:,:2]
y = wine.target
X_train,X_test,y_train,y_test = train_test_split(X,y)