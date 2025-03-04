"""
输入的第一行是开源项目数量
输入第二行是每个维度的权重值
从第三行开始表示项目名称，以及每个开源项目关注，收藏，fork,issue,MR的数量

5
5 6 6 1 2
camila 13 88 46 26 169
grace 64 38 87 23 103
lucas 91 79 98 154 79
leo 29 27 36 43 178
ava 29 27 36 43 178
"""
def originproject():
    N=int(input())
    weight=list(map(int,input().split()))
    project=dict()
    for i in range(N):
        lst=list(input().split())
        project[lst[0]]=list(map(int,lst[1:]))

    print(project)
    project_nums=dict()
    for key,value in project.items():
       project_nums[key]=sum(value[j]*weight[j] for j in range(len(value)))
    print(project_nums)
    sorted_pro=sorted(project_nums,key=lambda item:(-project_nums[item],item))
    print(sorted_pro)
    for ele in sorted_pro:
        print(ele)
    return 0
if __name__=="__main__":
    originproject()





        
