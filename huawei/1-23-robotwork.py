"""
机器人搬砖和猴子吃桃子类似

"""

def robotswork():
    bricks=list(map(int,input().split()))
    if(len(bricks)>8):
        result=-1
    if(len(bricks)==8):
        result=max(bricks)
    if(len(bricks)<8):
        for i in range(1,max(bricks)):
            time=0
            for j in range(len(bricks)):
                if(bricks[j]%i==0):
                    time+=bricks[j]//i
                if(bricks[j]%i!=0):
                    time+=bricks[j]//i+1
        #确保是最小的能量值
            if(time<=8):
                result=i
                break
    print(result)
    return result
    


if __name__=="__main__":
    robotswork()