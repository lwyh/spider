import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree,datasets
data = pd.read_csv('D:\\spider\\adult.csv',header=None,index_col=False,
                   names=['年龄','单位性质','权重','学历','受教育时长','婚姻状况','职业','家庭情况','种族','性别','资产所得','资产损失','周工作时长','原籍','收入'])
data_lite  = data[['年龄','单位性质','学历','性别','周工作时长','职业','收入']]

#print(data_lite.head(n=15))
#使用get_dummies将文本数据转化为数值
data_dummies = pd.get_dummies(data_lite)
#对比样本原始特征和虚拟变量特征
#print('样本原始特征:\n',list(data_lite.columns),'\n')
#print('虚拟变量特征:\n',list(data_dummies.columns))
#print(data_dummies.astype(int))
#定义数据集的特征值
features = data_dummies.loc[:,'年龄':'职业_ Transport-moving']
#将特征数值赋值为X
X= features.values
#将收入大于50K作为预测目标
y = data_dummies['收入_ >50K'].values



#将数据集拆分为训练集和测试集
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)
#用最大深度为5的随机森林拟合数据
go_dating_tree = tree.DecisionTreeClassifier(max_depth=5)
go_dating_tree.fit(X_train,y_train)

Mr_Z =  [[37,40,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
          

#使用模型做出预测
dating_dec = go_dating_tree.predict(Mr_Z)
         

print('\n\n\n')
print('代码运行结果：')
print('================================================\n')
#打印数据形态
print('特征形态:{} 标签形态:{}'.format(X.shape,y.shape))
print('模型得分:{:.2f}'.format(go_dating_tree.score(X_test,y_test)))
if(dating_dec ==1):
    print("大胆追爱吧")
else:
    print("不要费心思，不和合胃口")
print('\n================================================')
print('\n\n\n')



