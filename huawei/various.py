"""
题目描述

推荐多样性需要从多个列表中选择元素，一次性要返回N屏数据（窗口数量），每屏展示K个元素（窗口大小），选择策略：

    各个列表元素需要做穿插处理，即先从第一个列表中为每屏选择一个元素，再从第二个列表中为每屏选择一个元素，依次类推
    每个列表的元素尽量均分为N份，如果不够N个，也要全部分配完，参考样例图：
    （1）从第一个列表中选择4条0 1 2 3，分别放到4个窗口中
    （2）从第二个列表中选择4条10 11 12 13，分别放到4个窗口中
    （3）从第三个列表中选择4条20 21 22 23，分别放到4个窗口中

（4）再从第一个列表中选择4条4 5 6 7，分别放到4个窗口中
…
（5）再从第一个列表中选择，由于数量不足4条，取剩下的2条，放到窗口1和窗口2
（6）再从第二个列表中选择，由于数量不足4条并且总的元素数达到窗口要求，取18 19放到窗口3和窗口4




"""

def main():
    #读取输入的n和k
    n,k = int(input()),int(input())
    data = []
    #读取数据直到遇到异常
    while True:
        try:
            data.append(list(map(int,input().split(' '))))
        except:
            break
    index,t = 0,0
    arr ,temp = [],[]
    #从data元素中提取元素填充arr
    while t<k:
        cnt = 0
        for i in range(index,len(data)):
            for _ in range(len(data[i])):
                cnt +=1
                temp.append(data[i].pop(0))
                if len(temp) >=n:
                    break
            if len(temp) >=n:
                break
        index =(index+1) % len(data)
        if len(temp) ==n:
            t +=1
            arr.append(temp[:])
            temp.clear()
        elif cnt ==0:
            pass
        #处理剩余的元素
    if temp:
        arr.append(temp)
        #输出结果
    for i in range(n):
        for j in range(k):
            print(arr[j][i],end= " ")
    print()

if __name__ == '__main__':
    main()



