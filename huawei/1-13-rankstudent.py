"""
输入第一行表示学生人数和科目
输入第二行表示科目名称
从第三行起表示学生的姓名，科目分数
最后一行表示按照科目或者总分排名

"""
def rankstudent():
    lst=list(map(int,input().split()))
    n,m=lst[0],lst[1]
    subject=list(input().split())
    chengji=[]
    for i in range(n):
        chengji.append(list(input().split()))
    print(chengji)
    rank=input()
    student=dict()
    sorted_stu=[]
    #按照科目名称排名
    if(rank in subject):
        for i in range(len(subject)):
            if(subject[i]==rank):
                for j in range(len(chengji)):
                    student[chengji[j][0]]=int(chengji[j][i+1])
                sorted_stu=sorted(student,key=lambda item:(-student[item]))
    else:
        #按照总分排名
        if(rank=="zongfen"):
            for j in range(len(chengji)):
                    student[chengji[j][0]]=sum(list(map(int,chengji[j][1:])))
            sorted_stu=sorted(student,key=lambda item:(-student[item]))
   
    print(sorted_stu)
    result=" ".join(sorted_stu)
    print(result)
    return result

if __name__=="__main__":
    rankstudent()
    
    

