from sklearn.neural_network import MLPClassifier
#导入红酒数据集
from sklearn.datasets import load_wine

from sklearn.model_selection import train_test_split

wine = load_wine()

X = wine.data[:,:2]
y = wine.target
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)

mlp = MLPClassifier(solver='lbfgs')
mlp.fit(X_train,y_train)