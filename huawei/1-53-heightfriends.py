"""
寻找身高差从小到大的排列，身高差一样时，身高小的排在前面
100 10
95 96 97 98 99 101 102 103 104 105

"""
def heightfriends():
    lst=list(map(int,input().split()))
    H,N=lst[0],lst[1]
    lst2=list(map(int,input().split()))
    sorted_list=[]
    if(min(lst2)>=H):
        sorted_list=lst2.sort()
    if(max(lst2)<=H):
        sorted_list=lst2.sort(reverse=True)
    if(H>min(lst2) and H<max(lst2)):
        #主要是要注意循环的条件
        bigger=max(abs(max(lst2)-H),abs(min(lst2)-H))
        print(bigger)
        for i in range(bigger+1):
            similar_list=[]
            for j  in range(len(lst2)):
                if(abs(lst2[j]-H)==i ):
                    similar_list.append(lst2[j])
            if(similar_list!=[]):
                similar_list.sort()
                print("similar_list",similar_list)
                for  ele in similar_list:
                    sorted_list.append(ele )
            print("sorted_list",sorted_list)
    return sorted_list
if __name__=="__main__":
    heightfriends()
        

