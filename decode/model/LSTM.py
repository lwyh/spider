import pandas as pd
import matplotlib.pyplot as plt
import jenkspy
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.metrics import mean_squared_error
import numpy as np

data = pd.read_csv("D:\\second\\天气直播大屏\\最终代码\\数据\\new_weather_data_new.csv",encoding='utf-8')
data.columns=['Date','tianqi','fengxiang','max_wendu','min_wendu','aqilevel','aqiinfo']
print(data.head())
#将data列设为索引

#时间序列预测最高温度
#问题：如何预测非数字型的字段
selected_columns = ['Date','max_wendu']
new_data = data[selected_columns]
print(new_data.head())
series = new_data.set_index(['Date'],drop = True)
print(series)
plt.figure(figsize =(100,10))
series['max_wendu'].plot()
#plt.show()

#差分转换
def differnece(data_set,interval=1):
    diff = list()
    for i in range(interval,len(data_set)):
        value = data_set[i]-data_set[i-interval]
        diff.append(value)
    return pd.Series(diff)
#此处的series是之前数据预处理后得到的DateFrame型数据
raw_value = series.values
diff_value = differnece(raw_value,1)
print('diff_value',diff_value)

#将时间序列形式的数据转换为监督学习集的形式，例如：[[10],[11],[12],[13],[14]]转换为[[0,10],[10,11],[11,12],[12,13],[13,14]]，即把前一个数作为输入，后一个数作为对应输出。
def timeseries_to_supervised(data,lag=1):
    df = pd.DataFrame(data)
    columns = [df.shift(1)]
    #这两步缺一不可
    columns.append(df)
    df = pd.concat(columns,axis=1)
    #print('df',df)
    df.fillna(0,inplace=True)
    return df

supervised = timeseries_to_supervised(diff_value,1)
supervised_value = supervised.values

testNum = 360
train,test = supervised_value[:-testNum],supervised_value[-testNum:]
#将训练集和测试集中的数据都缩放到[-1,1]之间，可以加快收敛
def scale(train,test):
    #创建一个缩放器，将数据集中的数据缩放到[-1,1]的取值范围中
    scaler = MinMaxScaler(feature_range=(-1,1))
    #使用数据来训练来缩放器
    scaler =scaler.fit(train)
    #使用缩放器来将训练集和测试集进行缩放
    train_scaled = scaler.transform(train)
    test_scaled = scaler.transform(test)
    #print(train_scaled)
    return scaler,train_scaled,test_scaled

scaler,train_scaled,test_scaled = scale(train,test)
#print(scale(train,test))

#训练lstm模型
X,y=train[:,0:-1],train[:,-1]
X=X.reshape(X.shape[0],1,X.shape[1])

def fit_lstm(train,batch_size,nb_epoch,neurons):
    #将数据对中的x和y分开
    X,y=train[:,0:-1],train[:,-1]
    #将2D数据拼接成3D数据，形状为[N*1*1]
    X=X.reshape(X.shape[0],1,X.shape[1])

    model = Sequential()
    model.add(LSTM(neurons,input_shape=(batch_size,X.shape[1],X.shape[2]),stateful=True))
    #model.add(LSTM(neurons,input_shape=(batch_size,X.shape[1],X.shape[2]),stateful=True))
    model.add(Dense(1))

    model.compile(loss='mean_squared_error',optimizer = 'adam')
    for i in range(nb_epoch):
        #shulffle是不混淆数据顺序
        his = model.fit(X,y,batch_size=batch_size,verbose=1,shuffle=False)
  #      #每训练玩一次就重置一次网络状态,网络状态与网络权重不同
        model.reset_states()
    return model

#构建一个LSTM模型并训练，样本数为1，训练次数为3，LSTM层神经元个数为4
lstm_model = fit_lstm(train_scaled,1,3,4)


def forecast_lstm(model,batch_size,X):
    #将形状为[1:]的，包含一个元素的一维数组x，转换形状为[1,1,1]的3D张量
    X=X.reshape(1,1,len(X))
    #输出形状为一行一列的二维数组yhat
    #yhat = model.predict(X,batch_size=batch_size)
    #将yhat中的结果返回
    return yhat[0,0]


# 对预测的数据进行逆差分转换
def invert_difference(history,yhat,interval=1):
    return yhat+history[-interval]

# 将预测值进行逆缩放，使用之前训练好的缩放器，x为一维数组，y为实数
def invert_scale(scaler,X,y):
    # 将X,y转换为一个list列表
    new_row=[x for x in X]+[y]
    # 将列表转换为数组
    array=np.array(new_row)
    # 将数组重构成一个形状为[1,2]的二维数组->[[10,12]]
    array=array.reshape(1,len(array))
    # 逆缩放输入的形状为[1,2]，输出形状也是如此
    invert=scaler.inverse_transform(array)
    # 只需要返回y值即可
    return invert[0,-1]



predictions = list()
for i in range(len(test_scaled)):
    #将测试集拆分为X和y
    X,y = test[i,0:-1],test[i,-1]
    #将训练好的模型，测试数据传入预测函数中
    yhat = forecast_lstm(lstm_model,1,X)
    #将预测值进行逆缩放
    yhat = invert_scale(scaler,X,yhat)
    #对预测是y值进行逆差分
    yhat = invert_difference(raw_value,yhat,len(test_scaled)+1-i)
    #存储正在预测的y值
    predictions.append(yhat)
    #预测结果的可视化

    plt.plot(raw_value[-testNum:])
    plt.plot(predictions)
    plt.legend(['true','pred'])
    plt.show()







    

















#自然断点法
new_data = data['max_wendu']
breaks = jenkspy.jenks_breaks(new_data, n_classes=4)
#print(breaks)
groups = pd.cut(new_data,breaks,labels = False)
# 将数据分成4个级别
classes = []
for value in new_data:
    class_index = 0
    for i in range(len(breaks)-1):
        if value >= breaks[i] and value < breaks[i+1]:
            class_index = i
            break
        elif value >= breaks[-1]:
            class_index = len(breaks) - 2
            break
    classes.append(class_index+1)
#new_data.to_excel('result.xlsx')
data['classes'] = classes
#data.to_excel('result.xlsx', index=False)

