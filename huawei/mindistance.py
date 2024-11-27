"""
两个字符串以字母组合而成，从起点到终点得最短距离，当同一位置的字符相同时可以以斜边作为距离，

"""

from collections import defaultdict


def mindistance():
    step=0
    list1=[]
    list2=[]
    co_str=[]
    j=0
    arr=list(input().split())
    str1,str2=arr[0],arr[1]
    print(str1,str2)
    for i in range(len(str1)):
        #同一位置元素不同，向右移动一位交叉仍不相同
            if(str1[i:i+1]!=str2[i:i+1] and str1[i+1:i+2]!=str2[i:i+1]  and str1[i:i+1]!=str2[i+1:i+2]):
                print(str1[i:i+1],i,step)
                step+=2
                i+=1
                j=i
                if(i==len(str1)-1):
                    break
        #同一位置元素相同     
            if(str1[i:i+1]==str2[i:i+1]):
                print(str1[i:i+1],i,step)
                step+=1
                i+=1
                j=i
                if(i==len(str1)-1):
                    break
        # 同一位置元素不同，但向右移动一位右上和左下交叉元素相同
            if(str1[i:i+1]!=str2[i:i+1] and str1[i+1:i+2]==str2[i:i+1] ):
                print(str1[i:i+1],i,step)
                step+=2
                i+=2
                j=i
                if(i==len(str1)-1):
                    break
        # 同一位置元素不同，但向右移动一位左上和右下交叉元素相同       
            if(  str1[i:i+1]!=str2[i:i+1] and str1[i:i+1]==str2[i+1:i+2]):
                print(str1[i:i+1],i,step)
                step+=1
                i+=1
                j=i+1
                if(i==len(str1)-1):
                    break
        # 同一位置元素不同，但向左移动一位左下和右上交叉元素相同       
            if( str1[i:i+1]!=str2[i:i+1]  and str1[i:i+1]==str2[i-1:i]):
                print(str1[i:i+1],i,step)
                step+=1
                i+=1
                j=i
                if(i==len(str1)-1):
                    break
        #同一位置元素不同，且向右移动一位，右下元素为空，右上和左下交叉元素不同
            if(str1[i:i+1]!=str2[i:i+1]  and str1[i+1:i+2]!=str2[i:i+1]):
                print(str1[i:i+1],i,step)
                step+=2
                i+=1
                j=i+1
                if(i==len(str1)-1):
                    break
            
    if(len(str1)>len(str2)):
        step+=1
    else:
        if(str1[-1]==str2[-2]):
            step+=2
        if(str1[-1]!=str2[-2] and str1[-1]==str2[-1]):
            step+=1
        if(str1[-1]!=str2[-2] and str1[-1]!=str2[-1]):
            step+=2
        
               

    print(step)
    return step

if __name__=="__main__":
    mindistance()