"""
输入航班的信息
输出航班的起飞顺序

"""
def plainplan():
    plain_info=list(input().strip(" ").split(","))
    sorted_info = sorted(plain_info)
    result=",".join(sorted_info)
    print(result)
    return result
if __name__=="__main__":
    plainplan()