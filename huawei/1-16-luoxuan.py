"""
矩阵中含有数的个数n,行数m

"""
import numpy as np
def luoxuan():
    lst=list(map(int,input().split()))
    n,m=lst[0],lst[1]
    #确认n值时需要使用几行几列的矩阵表示
    if(n%m==0 and n>=m):
        col=n//m
    if(n<m):
        col=1
    if(n%m !=0 and n>=m):
        col=n//m+1
    print(m,col)
    #此处的矩阵类型必须为object，方便超出n的值使用*替代
    matrix=np.zeros((m,col),dtype=object)
    """
    #列数为1时的输出
    if(n<m):
        for i in range(m):
            if(i<n):
                matrix[i]=i+1
            else:
                matrix[i]='*'
    #列数不为1的情况，且个数仅围绕在第一圈
    if(n>=m and n<=(m+col)*2-4):
        for k in range(1,n+1):
            if(k<=col):
                subrow=0
                subcol=(k-1)%col
                matrix[subrow][subcol]=k
            if(k>col and k<=col+m-1):
                subrow=(k-col)%m
                subcol=col-1
                matrix[subrow][subcol]=k
            if(k>col+m-1 and k<=2*col+m-2):
                subrow=m-1
                subcol=(col-(k-(col+m-2)))%col
                matrix[subrow][subcol]=k
            if(k>2*col+m-2 and k<=n):
                subrow=m-(k-(2*col+m-3))
                subcol=0
                matrix[subrow][subcol]=k
    #列数不为1的情况，且个数围绕着矩阵不止一圈
    """
    value=1
    top,bottom,left,right=0,m-1,0,col-1
    state=False #退出外层循环的标志
    while value<=n:
        for i in range(left,right+1):#向右，每次循环完后圈的表示小一圈
            matrix[top][i]=value
            print(value,"right")
            #主要是判断是否达到n，如果达到后，需要先退出内层循环，然后再退出外层循环
            if(value==n):
                state=True
                break
            value+=1
        if(state==True):
            break
        top+=1
        for i in range(top,bottom+1):#向下
            matrix[i][right]=value
            print(value,"bottom")
            if(value==n):
                state=True
                break
            value+=1
        if(state==True):
            break
        right-=1
        for i in range(right,left-1,-1):#向左
            matrix[bottom][i]=value
            print(value,"left")
            if(value==n):
                state=True
                break
            value+=1
        if(state==True):
            break
        bottom-=1
        for i in range(bottom,top-1,-1):#向上
            matrix[i][left]=value
            print(value,"top")
            if(value==n):
                state=True
                break
            value+=1
        if(state==True):
            break
        left+=1

#将不在n值范围内的需要用*表示
    for i in range(m):
        for j in range(col):
           if(matrix[i][j]==0):
                matrix[i][j]='*'

#矩阵的输出表示也很重要
    for row in matrix:
        print(" ".join(map(str,row)))
    

if __name__=="__main__":
    luoxuan()
        
        
        

