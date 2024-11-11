"""
A,B玩抢7游戏，A先报起始数字X，B接下来报的数字Y,确保(X-Y<3),如此循环
"""
X = int(input())


def winon7(numA):
    winA=0
    winB=0
    count=1
    list_A=[numA]
    list_B=[]
    while count<=numA-6:
        for i in range(1,3):
            if(count %2==1):
                for value in list_A:
                    value=value-i
                    list_B.append(value)
            elif(count%2==0):
                for value in list_B:
                    value=value-i
                    list_A.append(value)
        count+=1
        print(list_A)
        if(count %2 ==1 and 7 in list_A):
            winA=len([index for index,value in enumerate(list_A) if value==7])
        elif(count %2 ==0 and 7 in list_B):
            winB=len([index for index,value in enumerate(list_B) if value==7])
            
            break

            
    print(winB)
    return winB

if __name__=="__main__":
    winon7(X)




        

    


    


       


