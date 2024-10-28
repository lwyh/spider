#导入红酒数据集
from sklearn.datasets import load_wine
#导入交叉验证工具
from sklearn.model_selection import cross_val_score
#导入用于分类的支持向量机模型
from sklearn.svm import SVC
#载入红酒数据集
wine  =load_wine()
#设置SVC核函数为linear
svc = SVC(kernel='linear')
#使用交叉验证法对SVC进行评分
scores = cross_val_score(svc,wine.data,wine.target,cv=3)

#打印结果
print('交叉验证得分:{}'.format(scores))

#使用.mean()来获得分数平均值
print('交叉验证平均分:{:.3f}'.format(scores.mean()))
#打印红酒数据集的分类标签
print('酒的分类标签:\n{}'.format(wine.target))

#导入随机差分工具
from sklearn.model_selection import ShuffleSplit
#设置拆分的分数为10个
shuffle_split = ShuffleSplit(test_size=.2,train_size=.7,n_splits=10)

#对拆分好的数据集进行交叉验证
scores = cross_val_score(svc,wine.data,wine.target,cv = shuffle_split)
#打印交叉验证得分
print('随机拆分交叉验证模型得分:\n{}'.format(scores))

#导入LeaveOneOut
from sklearn.model_selection import LeaveOneOut
#设置cv参数为LeaveOneOut
cv = LeaveOneOut()
#重新进行交叉验证
scores = cross_val_score(svc,wine.data,wine.target,cv = cv)
#打印迭代次数
print('迭代次数:{}'.format(len(scores)))
#打印评分结果
print("模型平均分：{}".format(scores.mean()))
