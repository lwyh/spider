"""
This is a multi-line comment with docstrings
 原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。
  

数据范围：保证输入的是合法的IP序列 

"""
import sys




a1 = input("")
a2 = input("")


"""
1.使用类来返回多个值：
class Result:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def get_values():
    a = 1
    b = 2
    return Result(a, b)

result = get_values()
print(result.a)  # 输出：1
print(result.b)  # 输出：2


我们定义了一个名为Result的类，它有两个属性a和b。
get_values函数返回了一个Result对象，
并将两个整数作为参数传递给Result类的构造函数
通过使用类，我们可以更灵活地处理返回的多个值，并可以对每个值进行进一步的操作

2.字典返回多个值
def get_values():
    a = 1
    b = 2
    return {'a': a, 'b': b}

result = get_values()
print(result)  # 输出：{'a': 1, 'b': 2}
print(result['a'])  # 输出：1
print(result['b'])  # 输出：2

3.列表或元组返回多个值
def get_values():
    a = 1
    b = 2
    return (a, b)

result = get_values()
print(result)  # 输出：(1, 2)
print(result[0])  # 输出：1
print(result[1])  # 输出：2

"""
class Result:
    def __init__(self,a,b):
        self.a = a
        self.b = b
def transfer():
    b=''
    #确保输入的是4个整数组成的ip
    if(a1.count('.')==3):
        subip = a1.split('.')
        for s in subip:
            #将每个整数转换成8位二进制，并且最后合成32位 二进制数
            m = '{:08b}'.format(int(s))
            b +=m
        #将二进制最后又转换成十进制
        dec = int(b,2)   
    #确保输入的是十进制数转化成4个十进制数的ip
    if(a2.count('.')==0):
        b =''
        l = list()
        e ='.'
        #十进制数转换成二进制，但并非32位
        d = '{:08b}'.format(int(a2))
        #将二进制数补全32位，并且是左补
        for i in range(8-len(d)%8):
            b +='0'
            i +=1
        d =b+d
        #将32位二进制按照8步长截取成4部分，并放进一个列表
        list1 = [d[i:i+8] for i in range(0,len(d),8)]
        #将二进制数的列表转换成十进制数的列表
        for j in range(len(list1)):
            ip =int(list1[j],2)
            l.append(str(ip))
        #将列表再转换成4个整数的ip形式，需要注意在转换过程中数字的类型，有的是str,有的是int
        strip = e.join(l)
        return Result(dec ,strip)

result = transfer()
print(result.a)
print(result.b)



