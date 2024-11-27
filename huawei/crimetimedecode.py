"""
输入的时间，中出现的数字重新组合成新的未来时刻，找出距离输入时间最近的组合时刻为罪犯的可能犯罪时间


"""

def crimetime(number):
    print(number)
    hh=number[0]*10+number[1]
    ss=number[2]*10+number[3]
    over_list=[]
    cor_list=[]
    mintime=0
    ruletime=""
    if(ss!=59):
        for i in range(len(number)):
            if(number[-1]<number[i] ):
                over_list.append(number[i])
        print(over_list)
        if(len(over_list)==0):
            ruletime="00:00"
        else:   
            mintime=min(over_list)
            ruletime=str(number[0])+str(number[1])+":"+str(number[2])+str(mintime)
        over_list=[]
    if(ss==59 and hh!=23):
        for i in range(len(number)):
            if(number[1]<number[i] ):
                over_list.append(number[i])
        if(len(over_list)==0):
            ruletime="00:00"
        else:
            if(number[0]==2):
                for j in range(len(over_list)):
                    if((number[0]*10+over_list[j])<=23):
                        cor_list.append(over_list[j])
                minhour=min(cor_list)
                minss=min(number)
                print(minhour,minss)
                ruletime=str(number[0]*10+minhour)+":"+str(minss)+str(minss)
            if(number[0]!=2):
                minhour=min(over_list)
                minss=min(number)
                ruletime=str(number[0])+str(minhour)+":"+str(minss)+str(minss)
        over_list=[]
            
    if(hh==23 and ss==59):
        ruletime="22:22"
   
    return ruletime
        

def main():
    time = input()
    number=[]
    if(len(time)<5):
        print("输入时间不合法")
    else:
        arr = time.split(":")
        hh,ss=arr[0],arr[1]
        for h in hh:
            number.append(int(h))
        for s in ss:
            number.append(int(s))
    out = crimetime(number)
    print(out)

    return out







if __name__=="__main__":
    main()

