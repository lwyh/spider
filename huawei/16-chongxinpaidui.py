import numpy as np



def chongxinpaidui():
    in1= input()
    in2= input()
    arr1 = in1.split(" ")
    arr2 = in2.split(" ")
    steps =3
    num=len(arr1)//steps
    two_d_arr1 = np.array(arr1).astype(int).reshape(-1,steps)  #目前学生排队情况
    two_d_arr2 = np.array(arr2).astype(int).reshape(-1,steps)   #目标学生分组情况
    count1=0 #3个都在一组的组数
    count2=0 #2个都在一起的组数
    count3=0 #每个都不在一组的组数
    count4=0 #3个都不在一组的组数

    for i in range(len(two_d_arr2)):
        for j in range(len(two_d_arr1)):
            if(set(two_d_arr1[j]) == set(two_d_arr2[i])):
                count1+=1
                continue
            if(len(set(two_d_arr2[i]) - set(two_d_arr1[j])) ==1):
                count2+=1
                continue
            if(len(set(two_d_arr1[j]) - set(two_d_arr2[i])) ==2):
                count3+=1
                continue
            if(len(set(two_d_arr1[j]) - set(two_d_arr2[i])) ==3):
                count4+=1
                continue

    #print(count1,count2,count3,count4)      
    if(count1==0 and count4==num):
        print(num)
    elif(count1==0 and count4!=num):
        print(num-1)
    elif(count1!=0 and count2!=0 ):
        print(num-count1-1)
    elif(count1!=0 and count2==0 ):
        print(num-count1)
    
    return count1,count2,count3,count4
    


if __name__ == '__main__':
    chongxinpaidui()





















