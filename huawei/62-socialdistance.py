"""
会议室的座位是确定的，1表示进场，-k表示座位K上的人离场，第一行表示会议室的总座位数，
第二行表示参与会议的人的进出场的数组
输出最后一位进场人员的座位

"""


def all_combine(seat,free_seat,array,used_seated,index):  
    #第一个元素       
    if(index==0):
        used_seated[0]=True  
        free_seat= [seat[k] for k in range(len(seat)) if used_seated[k]==True]  
        print("free_seat",free_seat)  
    #最后一个元素        
    if(index == 1 and array[index]==1): 
        out=N-1
        print(out,"out")
        used_seated[out]=True
        free_seat= [seat[k] for k in range(len(seat)) if used_seated[k]==True]
        print("free_seat",free_seat) 
    #中间元素出现负数
    if(index >=1 and index < len(array)-1 and  array[index]<0):
        if(used_seated[abs(array[index])]==True):
            print(abs(array[index]),"abs")
            used_seated[abs(array[index])]=False
            free_seat= [seat[k] for k in range(len(seat)) if used_seated[k]==True]
    #最后一个元素为负数
    if(index ==len(array)-1 and array[index]<0):
        if(used_seated[abs(array[index])]==True):
            print(abs(array[index]),"abs")
            used_seated[abs(array[index])]==False
            free_seat= [seat[k] for k in range(len(seat)) if used_seated[k]==True]
        return out   
    out_list=[]
    #中间元素是1
    if(index > 1 and  index <= len(array)-1  and array[index]==1):
        print(used_seated,"used_seated")
        print("free_seat",free_seat)
        free_seat=[seat[k] for k in range(len(seat)) if used_seated[k]==True]
        print("free_seat",free_seat)
        for i in range(len(free_seat)):
            for j in range(len(free_seat)):
                if(i!=j):
                    print((free_seat[i]+free_seat[j])//2)
                    out_list.append((free_seat[i]+free_seat[j])//2)
        print("out_list",out_list)
        out_list= list(set(out_list))
        print("out_list",out_list)
        #不符合条件的座位号需要去掉
        for ele in out_list[:]:
            print(ele)
            for l in range(len(free_seat)):
                if(abs(ele-free_seat[l]) <=1):
                    out_list.remove(ele)
                    break
        if(len(out_list)==1):
            print(out_list,"111")
            out= out_list[0]
            if(index==len(array)-1):
                return out 
            used_seated[out]=True
        if(len(out_list)>1):
            out= min(out_list)
            print(out_list,"222")
            print(index,"index")
            if(index==len(array)-1):
                print("out",out)
                return out
            used_seated[out]=True
        if(len(out_list)==0):
            out=-1
            return out 
    all_combine(seat,free_seat,array,used_seated,index+1)
                                        

if __name__=="__main__":
    N=int(input())
    array= list(map(int,input().split()))
    used_seated=[False]*N#占座的位置
    seat=[ele for ele in range(N)]#空座的位置
    all_combine(seat,[],array,used_seated,0)