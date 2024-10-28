from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
#导入画图工具
import matplotlib.pyplot as plt
import numpy as np
#导入学习曲线率
from sklearn.model_selection import learning_curve
#导入随机拆分工具
from sklearn.model_selection import ShuffleSplit
#定义一个函数绘制学习曲线
def plot_learning_curve(estimator,title,X,y,ylim = None,cv = None,n_jobs=1,train_sizes=np.linspace(.1,1.0,5)):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
#设定横轴标签
    plt.xlabel("Training example")
#设定纵轴标签
    plt.ylabel("Score")
    train_sizes,train_scores,test_scores  = learning_curve(estimator,X,y,cv = cv,
                                                       n_jobs=n_jobs,train_sizes = train_sizes)
    train_scores_mean = np.mean(train_scores,axis=1)
    test_scores_mean = np.mean(test_scores,axis=1)
    plt.grid()

    plt.plot(train_sizes,train_scores_mean,'o-',color="r",label = "Traning score")
    plt.plot(train_sizes,test_scores_mean,'o-',color="g",label = "Cross-valication-score")
    plt.legend(loc="lower right")
    return plt
#设定图题目
title= "Learning Curves (Naive Bayes)"
#设定拆分数量
cv = ShuffleSplit(n_splits=100,test_size=0.2,random_state=0)
#设定模型为高斯朴素贝叶斯
estimator = GaussianNB()
cancer = load_breast_cancer()
X,y = cancer.data,cancer.target
#调用我们定义好的函数
plot_learning_curve(estimator , title,X,y,ylim =(0.9,1.01),cv = cv ,n_jobs=4)
#显示图片
plt.show()



