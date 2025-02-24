"""
任意一个整数，如果能分解成两个素数之积，则输出两个数
如不能，则输出-1 -1

"""

def primedecomposition():
    N=int(input())
    for i in range(2,N//2+1):
        if(N%i==0):
            quoe=N//i
            if(i<quoe):
                if all(i%k !=0 for k in range(2,i)):
                    if all(quoe% m !=0 for m in range(2,quoe)):
                        print(i,quoe)
                    else:
                        print(-1,-1)
    return 0
if __name__=="__main__":
    primedecomposition()


