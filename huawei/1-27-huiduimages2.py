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
    for i in range(2,len(lst1)-1):
        if(i%2==0):
            images_lst.append([lst1[i],lst1[i+1]])
    print(images_lst)
    site=lst2[0]*10+lst2[1]+1
    sum_length=0
    result=0
    #累加值的表示,特殊情况是在第一个值的范围内
    for i in range(len(images_lst)-1):
        sum_length+=images_lst[i][1]
        if(site<=images_lst[0][1]):
            result=images_lst[0][0]
            break
        if(site>sum_length and site<=sum_length+images_lst[i+1][1]):
            print("sum_length",sum_length,images_lst[i+1][0])
            result=images_lst[i+1][0]
            break
    print(result)
    return result
if __name__=="__main__":
    huiduimages()





    








































