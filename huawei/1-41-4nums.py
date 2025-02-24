"""
每次每位数字位上遇到4就跳表，输入表的读数
输出车的实际产生费用

"""

def actualremotal():
    nums= int(input())
    def get_digit(num):
        return [int(digit) for digit in str(num)]
    def get_digits(num):
        digits=[]
        while num>0:
            digits.append(num % 10)
            num= num//10
        return digits[::-1]
    jumps=0
    for i in range(1,nums+1):
        if(get_digits(i).count(4)>0):
            jumps+=1
    actual = nums-jumps
    print(actual)
    return actual
if __name__=="__main__":
    actualremotal()

