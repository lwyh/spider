"""
寿司分配，输入的是n盘寿司的价格数组，可以赠送下一盘最近的寿司，每个价格的寿司可以无限供应
"""
def shousi():
    price=list(map(int,input().split()))
    two_price=price+price
    actual_price=[]
    for i in range(len(price)):
        for j in range(i+1,i+len(price)):
            if(two_price[j]<two_price[i]):
                actual_price.append((two_price[j]+two_price[i]))
                break
        if all(two_price[j]>=two_price[i] for j in range(i+1,len(price)+i)):
            actual_price.append(two_price[i])
            
    print(actual_price)
    result=" ".join(map(str,actual_price))
    print(result)
    return result
if __name__=="__main__":
    shousi()
            

