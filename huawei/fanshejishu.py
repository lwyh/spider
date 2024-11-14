"""
给定一个二维矩阵0，1，一个物体从给定的初始位置出发，在给定的速度下移动，遇到矩阵的边缘则发生镜面反射，无论物体经过0还是1，都不影响其速度
请计算并给出经过t时间单位后，物体经过1点的次数     
第一行输入初始信息是
w,h,x,y,sx,sy,t
第二行开始一共h行，为二维矩阵信息
w,h为矩阵的宽和高
x,y为起始位置
sx,sy为初始速度
t为经过的时间    

本题中有个规定的东西，就是1的位置，是x=2或者x=7

"""
import numpy as np
arr1 = list(map(int,input().split()))
w,h=arr1[0],arr1[1]
x,y=arr1[2],arr1[3]
sx,sy=arr1[4],arr1[5]
t= arr1[6]
matrix = np.zeros((h,w),dtype=int)
for i in range(len(matrix)):
    matrix[i]=list(map(int,input().split()))

print(w,h,x,y,sx,sy,t)
print(matrix)
"""
#物体到达矩阵边缘时的特征为x=0或11，或y=0或6
#第一次反射前的运动轨迹(t[0,1]),当t=1时，x=3,y=0，实现第一次反射
x=2+t
y=1-t
#第一次反射后，第二次反射前的运动轨迹(t[0,6])，当t=6时，x=9,y=6，实现第二次反射
x=3+t
y=t
#第二次反射后，第三次反射前的运动轨迹(t[0,2])，当t=2时，x=11,y=4，实现第三次反射
x=9+t
y=6-t
#第三次反射后，第四次反射前的运动轨迹(t[0,4])，当t=4时，x=7,y=0，完成第四次反射
x=11-t
y=4-t
#由于t=13所以需要在有限时间内确定运动轨迹

"""
def fanshecount(t):
        count=0
    #只经过一条轨迹，并根据初始速度确定第一次反射的边界，矩阵信息为1的位置是x=2或x=7
    #第一种情况是初始速度sx>0 and sy>0,此时第一次边界为x=w-1或者y=h-1,但是这其中如果把x,y的触碰点都考虑的话，会很复杂
    #后面抽丝剥茧，发现因为x,y轴上都是匀速运动，于是可以只需要计算物体在x轴方向的运动即可
    #这样就只需要分3种情况即可
    #sx>0,sx<0,sx=0
    #第一种情况，sx>0
        if(sx>0 and t<w-1-x):
            X=x+sx*t
            if(X==2 or X==7):
                count+=1
        if(sx>0 and t>=w-1-x):
            if(x<=2 and x>=0):
                count+=2
            if(x<=7 and x>2):
                count+=1
            if(x>7 and x<=w-1):
                count
            a=(t-(w-1-x))//(w-1)
            b=(t-(w-1-x))%(w-1)
            print(a,b)
            if(a%2==0 and b>0 and b<4):
                count=count+a*2
            if(a%2==0 and b>=4 and b<9):
                count=count+a*2+1
            if(a%2==0 and b>=9 and b<w-1):
                count=count+a*2+2
            if(a%2==1 and b>0 and b<2):
                count=count+a*2
            if(a%2==1 and b>=2 and b<7):
                count=count+a*2+1
            if(a%2==1 and b>=7 and b<w-1):
                count=count+a*2+2
        #第二种情况，sx<0
        if(sx<0 and t<x):
            X=x-sx*t
            if(X==2 or X==7):
                count+=1
        if(sx<0 and t>=x):
            if(x<2 and x>=0):
                count
            if(x<7 and x>=2):
                count+=1
            if(x>=7 and x<=w-1):
                count+=2
            a=(t-x)//(w-1)
            b=(t-x)%(w-1)
            if(a%2==0 and b>=0 and b<2):
                count=count+2*a
            if(a%2==0 and b>=2 and b<7):
                count=count+2*a+1
            if(a%2==0 and b>=7 and b<w-1):
                count=count+2*a+2
            if(a%2==1 and b>=0 and b<4):
                count=count+2*a
            if(a%2==1 and b>=4 and b<9):
                count=count+2*a+1
            if(a%2==1 and b>=9 and b<w-1):
                count=count+2*a+2
        #第三种情况，sx=0
        if(sx==0 and sy!=0):
            if(x==2 or x==7):
                count=t+1
            else:
                count
        print(count)
        return count
if __name__=="__main__":
    fanshecount(t)


            


            
        



        




          


    










