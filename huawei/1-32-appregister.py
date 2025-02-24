"""
app的注册时间段，在同一时间段内不能有多个app注册使用，只能是一个app
优先级越高的在交叉时间内会优先注册，优先级较低的会被注销
同时优先级相同时，则先被注册的app使用，后添加的app不能被注册
输出在某个时间点可以使用的app
NA表示空闲时间即没有可用的app

"""
from datetime import datetime
def appregister():
    N=int(input())
    app_list=[]
    for i in range(N):
        app_list.append(list(input().split()))
    print(app_list)
    time1=str(input())
    time_format="%H:%M"
    time_std=datetime.strptime(time1,time_format).time()
    print("time_std",time_std)
    app_dict=dict()
    if(len(app_list)==1):
        app_dict[app_list[0][0]]=[datetime.strptime(app_list[0][2],time_format).time(),datetime.strptime(app_list[0][3],time_format).time()]
    else:
        for i in range(len(app_list)-1):
            start_time,end_time = datetime.strptime(app_list[i][2],time_format).time(),datetime.strptime(app_list[i][3],time_format).time()
            if(app_list[i][0] not in app_dict):
                app_dict[app_list[i][0]]=[[start_time,end_time]]
            else:
                max_nums = max([ele for sublist in app_dict[app_list[i][0]] for ele in sublist])
                if(start_time>=max_nums):
                    app_dict[app_list[i][0]].append([start_time,end_time])
            #[start_time,end_time] i 包含[start_time,end_time] i+1区间，且app1级别小于app2
            if(datetime.strptime(app_list[i+1][2],time_format).time() >=start_time and datetime.strptime(app_list[i+1][3],time_format).time()<=end_time
            and int(app_list[i][1])<int(app_list[i+1][1])):         
                app_dict[app_list[i][0]][-1]=[start_time,datetime.strptime(app_list[i+1][2],time_format).time()]
                if(app_list[i+1][0] not in app_dict):
                    app_dict[app_list[i+1][0]]=[[datetime.strptime(app_list[i+1][2],time_format).time(),datetime.strptime(app_list[i+1][3],time_format).time()]]
                else:
                    app_dict[app_list[i+1][0]][-1]=[datetime.strptime(app_list[i+1][2],time_format).time(),datetime.strptime(app_list[i+1][3],time_format).time()]      

                if("NA" not in app_dict):
                    app_dict["NA"]=[[datetime.strptime(app_list[i+1][3],time_format).time(),end_time]]
                else:
                    app_dict["NA"][-1]=[datetime.strptime(app_list[i+1][3],time_format).time(),end_time]
            if(datetime.strptime(app_list[i+1][2],time_format).time() >=start_time and datetime.strptime(app_list[i+1][3],time_format).time()<=end_time
            and int(app_list[i][1])>=int(app_list[i+1][1])):
                continue
            if(datetime.strptime(app_list[i+1][2],time_format).time() <end_time and datetime.strptime(app_list[i+1][3],time_format).time()>=end_time
            and int(app_list[i][1])<int(app_list[i+1][1])):
                app_dict[app_list[i][0]][-1]=[start_time,datetime.strptime(app_list[i+1][2],time_format).time()]
                if(app_list[i+1][0] not in app_dict):
                    app_dict[app_list[i+1][0]]=[[datetime.strptime(app_list[i+1][2],time_format).time(),datetime.strptime(app_list[i+1][3],time_format).time()]]
                else:
                    app_dict[app_list[i+1][0]][-1]=[datetime.strptime(app_list[i+1][2],time_format).time(),datetime.strptime(app_list[i+1][3],time_format).time()]
            if(datetime.strptime(app_list[i+1][2],time_format).time() <end_time and datetime.strptime(app_list[i+1][3],time_format).time()>=end_time
            and int(app_list[i][1])>=int(app_list[i+1][1])):
                if("NA" not in app_dict):
                    app_dict["NA"]=[[end_time,datetime.strptime(app_list[i+1][3],time_format).time()]]
                else:
                    app_dict["NA"][-1]=[end_time,datetime.strptime(app_list[i+1][3],time_format).time()]
            if(datetime.strptime(app_list[i+1][2],time_format).time() ==end_time ):
                if(app_list[i+1][0] not in app_dict):
                    app_dict[app_list[i+1][0]]=[[datetime.strptime(app_list[i+1][2],time_format).time(), datetime.strptime(app_list[i+1][3],time_format).time()]]
                else:
                    app_dict[app_list[i+1][0]].append([datetime.strptime(app_list[i+1][2],time_format).time(), datetime.strptime(app_list[i+1][3],time_format).time()])
            if(datetime.strptime(app_list[i+1][2],time_format).time() >end_time ):
                if("NA" not in app_dict):     
                    app_dict["NA"]=[[end_time,datetime.strptime(app_list[i+1][2],time_format).time()]]
                else:
                    #对于NA的更新需要分情况讨论，能覆盖的，需要追加的
                    max_nums = max([ele for sublist in app_dict["NA"] for ele in sublist])
                    if(datetime.strptime(app_list[i+1][2],time_format).time()<max_nums):
                        app_dict["NA"][-1]=[end_time,datetime.strptime(app_list[i+1][2],time_format).time()]
                    else:
                        app_dict["NA"].append([end_time,datetime.strptime(app_list[i+1][2],time_format).time()])
                if(app_list[i+1][0] not in app_dict):
                    app_dict[app_list[i+1][0]]=[[datetime.strptime(app_list[i+1][2],time_format).time(), datetime.strptime(app_list[i+1][3],time_format).time()]]
                else:
                    app_dict[app_list[i+1][0]].append([datetime.strptime(app_list[i+1][2],time_format).time(), datetime.strptime(app_list[i+1][3],time_format).time()])


    print("app_dict",app_dict)
    app_names=[]
    print(list(app_dict.keys()))
    
    for key,value in app_dict.items():
        #对于value大部分情况下其实并不是简单的list而是嵌套的list
        for l in range(len(value)):    
            if(key !="NA" and time_std>=value[l][0] and time_std<value[l][1]  ):
                app_names.append(key)
            else:
                app_names.append("NA")
    if all(app_names[k]=="NA" for k in range(len(app_names))):
        out=["NA"]
    else:
        out=[ele for ele in app_names if ele !="NA"]
    print(out)
    appNames=" ".join(out)
    
    print(appNames)
    return appNames

if __name__=="__main__":
    appregister()
