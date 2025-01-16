"""
每次都是取新队列的行首和行尾的最大值
"""

def maxnumber():
    m=int(input())
    numbers=[]
    numbers=list(map(int,input().split()))
    print("numbers",numbers)
    N=int(input())
    avialble_max=[]
    maxnumber=0
    if(N==1):
        maxnumber=max(numbers[0],numbers[-1])
    if(N>=len(numbers)):
        maxnumber=sum(numbers)
    if(N>1 and N<len(numbers)):
        count=0
        while count<N:
            if(numbers[0]>numbers[-1]):
                avialble_max.append(numbers[0])
                numbers.pop(0)
                count+=1
                continue
            if(numbers[0]<numbers[-1]):
                avialble_max.append(numbers[-1])
                numbers.pop()
                count+=1
                continue
            #本题比较复杂的一种情况就说当列表的首位元素相等时，需要一直继续比较下去，然后就说每次取出一个较大值后需要更新相应的状态
            #然后就是循环的次数
            if(numbers[0]==numbers[-1]):
                start=0
                end =len(numbers)-1
                while start < end and numbers[start]==numbers[end]:
                    start+=1
                    end-=1
                if (start == end or numbers[start] > numbers[end]):
                    max_element=numbers[0]
                    numbers.pop(0)
                    count+=1
                else:
                    max_element=numbers[-1]
                    numbers.pop(-1)
                    count+=1

                avialble_max.append(max_element)
                continue

                

        print(avialble_max,"avialble_max")
        maxnumber=sum(avialble_max)
    print(maxnumber)
    return maxnumber

if __name__=="__main__":
    maxnumber()

