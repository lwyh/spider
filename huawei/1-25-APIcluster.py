"""
输入的N个url位置，
/A/B/C/D分别表示的是第一，第二，第三，第四级别
最后一行输入是层级L和要查询的关键字
输出在指定层级上关键字出现的频次，使用的完全匹配的方式（大小写敏感）

"""
def APIcluster():
    N=int(input())
    url_lst=[]
    for i in range(N):
        url_lst.append(input())
    print(url_lst)
    #注意输入的既有数字又有字符类型时的不同之处
    last_lst=list(input().split())
    level,keyword =int(last_lst[0]),last_lst[1]
    count=0
    for i in range(len(url_lst)):
        url_level =url_lst[i].strip("/").split("/")
        if(len(url_level)>=level and url_level[level-1]==keyword):
            count+=1
    print(count)
    return count
if __name__=="__main__":
    APIcluster()

