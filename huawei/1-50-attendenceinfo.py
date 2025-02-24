"""
缺勤不超过一次
没有连续的迟到/早退，
任意连续7次考勤，缺勤/迟到。早退不超过3次

2
present
present absent present present leaveearly present late


"""
def attendenceinfo():
    N=int(input())
    attendence=[]
    for i in range(N):
        attendence.append(input().split())
    print(attendence)
    bool_list=[]
    for i in range(len(attendence)):
        if(len(attendence[i])==1):
            if(attendence[i][0]=="present"):
                bool_list.append("true")
            else:
                bool_list.append("false")
        if(len(attendence[i])>1 and len(attendence[i])<7):
            if all(attendence[i].count("absent")<=1 and not (attendence[i][j] in ["late", "leaveearly"] and attendence[i][j+1] in ["late","leaveearly"])  for j in range(len(attendence[i])-1)):
                bool_list.append("true")
            else:
                bool_list.append("false")
        count=0
        if(len(attendence[i])>=7 and len(attendence[i])<=10000): 
            #本题主要是对出勤信息的逻辑判断在任意连续的7次出勤信息中，缺勤/迟到/早退的次数不超过3次
            if all(attendence[i].count("absent")<=1 and not (attendence[i][j] in ["late", "leaveearly"] and attendence[i][j+1] in ["late","leaveearly"]) for j in range(len(attendence[i])-1)):
                if (all((attendence[i][l:l+7].count("absent")+attendence[i][l:l+7].count("late")+attendence[i][l:l+7].count("leaveearly"))<=3 for l in range(len(attendence[i])-7) if l+7<len(attendence[i]))
                   and all((attendence[i][l:].count("absent")+attendence[i][l:].count("late")+attendence[i][l:].count("leaveearly"))<=3 for l in range(len(attendence[i])-7) if l+7>=len(attendence[i]))):
                    bool_list.append("true")
                    count+=1
                    print("count",count)
                else:
                    bool_list.append("false")
            else:
                bool_list.append("false")
    print("bool_list",bool_list)
    out = " ".join(bool_list)
    print(out)
    return out

if __name__=="__main__":
    attendenceinfo()



                

