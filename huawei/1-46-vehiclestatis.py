"""
1表示有车，0表示没车，，小车占一个长度，货车占2个车位，卡车占3个车位
输出至少停车的车辆数
"""
import itertools
def vehiclestatis():
    lst=list(map(int,input().split(",")))
    delimiter=0
    groups=[list(group) for key ,group in itertools.groupby(lst,key=lambda 
    x: x!=delimiter) if key]
    print(groups)
    nums=0
    for i in range(len(groups)):
        if(len(groups[i])%3==0):
            nums+=len(groups[i])//3
        else:
            nums+=len(groups[i])//3+1
    print(nums)
    return nums
 
if __name__=="__main__":
    vehiclestatis()