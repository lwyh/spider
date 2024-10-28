from sklearn.datasets import load_files
import numpy as np
train_set = load_files('D:\\stock_database\\Imdblite\\train')
X_train, y_train = train_set.data, train_set.target
from sklearn.feature_extraction.text import CountVectorizer
#打印数据集文件数量
print('训练集文件数量:{}'.format(len(X_train)))

#将文本中的<br/>全部去掉
X_train =[doc.replace(b'<br />',b' ') for doc in X_train]

#随便抽取一条影评打印出来
print('随机抽一个看看:',X_train[22])

#载入测试集
test = load_files('D:\\stock_database\\Imdblite\\test')
X_test, y_test = test.data, test.target
#同样替换掉<br/>
X_test =[doc.replace(b'<br />',b' ') for doc in X_test]
#返回测试数据集中文件数量
print('测试集文件数量:{}'.format(len(X_test)))



#用CountVrctorizer拟合训练数据
vect = CountVectorizer().fit(X_train)
#将文本转化为向量
X_train_vect = vect.transform(X_train)
#打印训练集特征数量
print('训练集特征数量:{}'.format(len(vect.get_feature_names_out())))
#打印最后10个训练集样本特征
print('训练集最后10个样本特征:{}'.format(vect.get_feature_names_out()[-10:]))

#有监督进行交叉验证
#导入线性SVC分类模型
from sklearn.svm import LinearSVC
#导入交叉验证工具
from sklearn.model_selection import cross_val_score
#使用交叉验证模型进行评分
scores = cross_val_score(LinearSVC(), X_train_vect, y_train, cv=5)
#打印交叉验证平均分
print('模型平均分:{:.3f}'.format(scores.mean()))


#把测试数据集转化成向量
X_test_vect = vect.transform(X_test)
#使用线性SVC拟合训练数据集
clf = LinearSVC().fit(X_train_vect, y_train)
#打印测试数据集的得分
print('测试集得分:{}'.format(clf.score(X_test_vect, y_test)))


#导入tfidf转化工具
from sklearn.feature_extraction.text import TfidfTransformer
#用tfidf工具转化训练集和测试集
tfidf = TfidfTransformer(smooth_idf=False)
tfidf.fit(X_train_vect)
X_train_tfidf = tfidf.transform(X_train_vect)
X_test_tfidf = tfidf.transform(X_test_vect)
#将处理后的特征打印进行比较
print('未经tfidf处理的特征:\n',X_train_vect[:5,:5].toarray())
print('经过tfidf处理的特征:\n',X_train_tfidf[:5,:5].toarray())


#重新训练线性SVC模型
clf = LinearSVC().fit(X_train_tfidf,y_train)
#使用新数据进行交叉验证
scores2  = cross_val_score(LinearSVC(),X_train_tfidf,y_train)
#打印新的分数进行对比
print('经过tf-idf处理的训练集交叉验证得分:{:.3f}'.format(scores.mean()))
print('经过tf-idf处理的测试集得分:{:.3f}'.format(clf.score(X_test_tfidf,y_test)))


#导入内置的停用词库
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
#打印停用词个数
print('停用词个数: ',len(ENGLISH_STOP_WORDS))

#打印停用词中前20个和后20个
print('列出前20个和最后20个: \n',list(ENGLISH_STOP_WORDS)[:20],
      list(ENGLISH_STOP_WORDS)[-20:])


#导入Ffidf模型
from sklearn.feature_extraction.text import TfidfVectorizer
#激活英语停用词参数
tfidf = TfidfVectorizer(smooth_idf=False,stop_words='english')

#拟合训练数据集
tfidf.fit(X_train)
#将训练数据集文本转化成向量
X_train_tfidf = tfidf.transform(X_train)
#使用交叉验证进行评分
scores3 = cross_val_score(LinearSVC(),X_train_tfidf,y_train)
clf.fit(X_train_tfidf,y_train)
#将测试数据集转化成向量
X_test_tfidf = tfidf.transform(X_test)
#打印交叉验证评分和测试集评分
print('去掉停用词后训练集交叉验证平均分；{:.3f}'.format(scores3.mean()))
print('去掉停用词后测试集模型得分;{:.3f}'.format(clf.score(X_test_tfidf,y_test)))
