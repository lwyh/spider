"""
题目 运输时间
难度 难
题目说明 M（1<=M<=20）辆车需要在一条不能超车的单行道到达终点，起点到终点的距离为N（1<=N<=400）。速度快的车追上前车后，只能以前车的速度继续行驶。求最后一车辆到达目的地花费的时间。
注：每辆车固定间隔一小时出发，比如第一辆车0时出发，第二辆车1时出发，以此类推。
输入描述 第一行两个数字：M N分别代表车辆数和到终点的距离，以空格分隔。
接下来M行，每行1个数字S，代表每辆车的速度。0<S<30。
输出描述 最后一辆车到达目的地花费的时间。
补充说明 无
示例
示例1
输入 2 11
3
2
输出 5.5
说明 2 辆车，距离 11，0 时出发的车速度快，1 时出发的车，到达目的的花费为 5.5。

题目解答

从 0 时开始，依次计算每辆车需要的时间，由于后发的车速度较快，如果后发的车赶上前车，则到达时间为前车时间减 1 。从第 1 辆车开始，一直算到最后一辆车。时间复杂度为 O(n)，空间复杂为 O(n)。



"""


def process_transport_time(m, n, speed_list):
    print(m, n, speed_list)
    #最后一辆车追不上倒数第二辆
    if(speed_list[-2]>speed_list[-1]):
        time=n/speed_list[-1]
        print(time)
        return time
    #最后一辆车可以追上，先求最慢的车到达目的地的时间，然后减去距离最后一辆车的间隔时间
    else:
        longtime=n/min(speed_list)
        for i in range(len(speed_list)):
            if(speed_list[i]==min(speed_list)):
                mintime=longtime-(len(speed_list)-1-i)
        print(mintime)
        return mintime
        



if __name__=="__main__":
    list1=list(map(int,input().split()))
    m,n=list1[0],list1[1] #车辆数，起终点距离
    speed_list=[] #速度列表
    for i in range(m):
        speed_list.append(int(input()))
    print(m,n,speed_list)
    process_transport_time(m,n,speed_list)
  