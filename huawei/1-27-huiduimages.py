"""
图像像素恢复
输入的第一行是一组数组，前两个数表示的是矩阵的行和列
从第三个数开始，每两个数一组，每组第一个数是灰阶值，第二个数表示该灰阶值从左到右
从上到下的连续像素个数
输入第二行输入表示一个像素的行号和列号

输出第二行输入位置的灰阶值

"""
def huiduimages():
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    m,n=lst1[0],lst1[1]
    images_lst=[]
    for i in range(2,len(lst1)):
        if(i % 2 == 0 ):
            images_lst.append([lst1[i],lst1[i+1]])
    print(images_lst)
    images_dict=dict()
    if(images_lst[0][1]%n==0):
        row=images_lst[0][1]//n-1
        col=n-1
        images_dict[(row,col)]=images_lst[0][0]
    if(images_lst[0][1] %n!=0 and images_lst[0][1]<n):
        row=0
        col=images_lst[0][1]-1
        images_dict[(row,col)]=images_lst[0][0]
    if(images_lst[0][1] %n!=0 and images_lst[0][1]>n):
        row=images_lst[0][1]//n
        col=images_lst[0][1]%n-1
        images_dict[(row,col)]=images_lst[0][0]

    for start,end in images_lst[1:]:
        if(end % n !=0 and col+end<n):
            col +=end
            images_dict[(row,col)]=start
            continue
        if(end % n !=0 and col+end>=n):
            if(end<n):   
                row+=1
                col=col+end-n
                images_dict[(row,col)]=start
                continue
            if(end>n):
                row+=end//n
                col=col+end-n*(end//n)
                images_dict[(row,col)]=start  
                continue 
        if(end % n ==0):
            row+=end//n-1
            col=col
            images_dict[(row,col)]=start
            continue
    print("images_dict",images_dict)
    #输出指定行列的灰度值
    images_keys=list(images_dict.keys())
    






if __name__=="__main__":
    huiduimages()

































