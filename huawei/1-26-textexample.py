"""
输入第一行是N,M表示特征数量以及测试用例的数量
接下来的N行，表是N个特征的优先级
接下来的M行表示M个测试用例关联的特征列表

"""

def testexaple():
    lst=list(map(int,input().split()))
    N,M=lst[0],lst[1]
    rank_lst=[]
    for i in range(N):
        rank_lst.append(int(input()))
    test_lst=[]
    print(rank_lst)
    for j in range(M):
        test_lst.append(list(map(int,input().split())))
    print(test_lst)
    test_priority=[]
    #注意累加和的变量的迭代
    for j in range(M):
        test_priority.append(sum(rank_lst[ele-1] for ele in test_lst[j]))
    print(test_priority)
    test_priority_dict=dict()
    for idx,ele in enumerate(test_priority):
        test_priority_dict[idx+1]=ele
    sorted_priority_lst =sorted(test_priority_dict,key=lambda item:(-test_priority_dict[item],item))
    for ele in sorted_priority_lst:
        print(ele)
    return 0

if __name__=="__main__":
    testexaple()



