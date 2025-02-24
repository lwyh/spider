"""
 输入[nums],jumps,left，nums位数组，jumps是跳过的数的个数，left是最终留下来的数的个数
 输出left的数的之和

"""

def leftnumbers():
    lst = input().split("],")
    nums=[ele for ele in list(map(int,lst[0].strip("[]").split(",")))]
    print("nums", nums)
    jumps_left=list(map(int,lst[1].split(",")))
    jump=jumps_left[0]
    left=jumps_left[1]
    print("jumps",jump,left)
    length=len(nums)
    i=0
    while(len(nums)>left):
        if(i==0):
            nums.pop(i+jump+1)
            i+=jump+1
            print("nums",nums,i)
        if(i!=0 and i+jump<len(nums)):
            nums.pop(i+jump)
            i+=jump
            print("nums",nums,i)
        if(i+jump>=len(nums)):
            i=i+jump-len(nums)
            if(i<len(nums)):
                nums.pop(i)
            print("nums",nums,i)
    print(nums)
    sums=sum(nums)
    print(sums)
    
    return 0

if __name__=="__main__":
    leftnumbers()



