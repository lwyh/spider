"""
设计一个缓存文件系统，包括文件存储和文件读取，文件存储则是将文件放进缓存中，当缓存不够时，需要先删除缓存中的文件，直到空间足够再放进缓存，
删除的规则是:先删除缓存中访问次数较少的文件，再删除最近访问文件时间较老的文件
新文件名若与缓存中已有的文件名相同，则不会放在缓存中
新的文件第一次存入到缓存中，文件的访问次数不会变化，文件的最近访问时间会更新到最新时间
每次访问文件后，总访问次数加1，最近访问时间更新为最新时间
任何两个文件的最近访问时间不会重复
文件名不会为空，均为小写字母，最大长度为10
缓存空间不足时，不能存放新文件


"""
#from datetime import datetime
#import time
def cachesystem():
    maxsize= int(input())
    op_num= int(input())
    arr=[]
    file_info=dict()
    visit_count=dict()
    visit_updatetime=dict()
    list_name=[]
    count=0
    delete_key=[]
    for i in range(op_num):
        arr.append(input().split())
        i+=1
    #print(arr)
    if(arr[0][0]=="get"):
        print("NONE")
        return None
    for j in range(op_num):
        if(arr[j][0]=="put"):   
            #文件缓存剩余空间小于需要存放的文件大小，前提条件是文件名不重复
            while(int(arr[j][2])>maxsize):
                if(int(arr[j][2])>maxsize and arr[j][1] not in file_info.keys()):
                    min_key=[key for key,value in visit_count.items() if value==min(visit_count.values())]
                    if(len(min_key)>1):
                        min_update_dict={key:value for key,value in visit_updatetime.items() if key in min_key}
                        delete_key=min(min_update_dict,key = lambda k: min_update_dict[k])
                    if(len(min_key)==1):
                        delete_key=min_key
                    #当没有文件的访问次数时，需要根据文件的更新时间来确认删除的文件
                    if(len(min_key)==0):
                        delete_key=min(visit_updatetime,key = lambda k: visit_updatetime[k])
                    print(delete_key[0])
                    list_name=[key for key in file_info.keys()]
                    list_name.remove(delete_key[0])
                    print(list_name)
                    maxsize =maxsize+ file_info[delete_key[0]]
            if(int(arr[j][2])<=maxsize and arr[j][1] not in file_info.keys()):
                maxsize=maxsize-int(arr[j][2])
                file_info[arr[j][1]]=int(arr[j][2])
                visit_updatetime[arr[j][1]]=j 
                list_name.append(arr[j][1])           
            if(arr[j][1]  in file_info.keys()):
                maxsize=maxsize
        if(j!=0 and arr[j][0]=="get" ):
            if(arr[j][1] in file_info.keys()):
            #当文件已存在于访问文件的dict中时，需要累加访问次数，当不存在访问文件dict中时，赋值访问次数为1
                if(arr[j][1] in  visit_count.keys()):
                    visit_count[arr[j][1]]+=1
                else:
                    visit_count[arr[j][1]] =1
            #无论是访问文件还是存储文件，文件更新时间都需要更新，在此将文件操作的索引大小来代表更新时间的大小，也可以引入time模块
                visit_updatetime[arr[j][1]]=j
                #visit_updatetime[arr[j][1]]=time.time()
                #isit_updatetime[arr[j][1]]=datetime.now()
    print(list_name) 
    out=" ".join(list_name)
    print(out)
    return out


if __name__=="__main__":
    cachesystem()                   


    








 