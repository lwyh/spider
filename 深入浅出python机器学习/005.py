from sklearn.naive_bayes import BernoulliNB
import numpy as np
clf = BernoulliNB()
#将X,yf赋值为np数组
X = np.array([[0,1,0,1],
              [1,1,1,0],
              [0,1,1,0],
              [0,0,0,1],
              [0,1,1,0],
              [0,1,0,1],
              [1,0,0,1]])
y=np.array([0,1,1,0,1,0,0])
clf.fit(X,y)
Next_Day = [[0,0,1,0]]
pre = clf.predict(Next_Day)
print('\n\n\n')
print('代码运行结果：')
print('================================================\n')
if pre ==[1]:
    print("要下雨啦，快收衣服！")
else:
    print("放心，又是一个艳阳天")
print('================================================\n')
print('\n\n\n')

print(clf.predict_proba(Next_Day))
print('================================================\n')
print('\n\n\n')