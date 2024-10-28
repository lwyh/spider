from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.decomposition import NMF
#https://blog.csdn.net/m0_60465900/article/details/129748445    fetch_lfw_people数据集无法导入，权限问题解决方案  
faces = fetch_lfw_people(data_home= "D:\\spider\\深入浅出python机器学习\\",download_if_missing=False,min_faces_per_person=20,resize=0.8)
print(faces.keys())
image_shape = faces.images[0].shape

fig ,axes = plt.subplots(3,4,figsize=(12,9),subplot_kw = {'xticks':(),'yticks':()})

for target,image,ax in zip(faces.target,faces.images,axes.ravel()):
    ax.imshow(image,cmap=plt.cm.gray)
ax.set_title(faces.target_names[target])

X_train,X_test,y_train,y_test = train_test_split(faces.data/255.,faces.target,random_state=62)
#训练神经网络
mlp = MLPClassifier(hidden_layer_sizes=[100,100],random_state=62,max_iter=400)

#print('模型识别准确率:{:.2f}'.format(mlp.score(X_test,y_test)))
#使用白化功能处理人脸数据
pca = PCA(whiten=True,n_components=0.9,random_state=62).fit(X_train)
X_train_whiten  = pca.transform(X_train)
X_test_whiten = pca.transform(X_test)
#打印白化后数据形态
#print('白化后数据形态:{}'.format(X_train_whiten.shape))
    #显示图像
#plt.show()
mlp.fit(X_train_whiten,y_train)
print('数据白热化后模型识别准确率:{:.2f}'.format(mlp.score(X_test_whiten,y_test)))
nmf = NMF(n_components=105,random_state=62).fit(X_train)
X_train_nmf = nmf.transform(X_train)
X_test_nmf = nmf.transform(X_test)
#打印NMF处理后的数据形态
print('NMF处理后数据形态:{}'.format(X_train_nmf.shape))

mlp.fit(X_train_nmf,y_train)

print('nmf处理后的模型准确率：{:.2f}'.format(mlp.score(X_test_nmf,y_test)))