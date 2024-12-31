"""
根据两段字符串对比，判断相似字符是否成立，相似字符具有传递性，相似字符组如果有存在两组字符串中，则成立，或者通过传递性也能成立


"""

def stringrepeat():
    str1=input()
    str2=input()
    arr=[] 
    while len(arr)<10:
        user_input=input()
        if(user_input==""):
            break
        arr.append(list(user_input.split()))     
    print("arr",arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            #"(***)"可以表示任意的相似字符的表达
            if(arr[i][j]=="(***)" and (str1 ==str2[0:len(str1)] or str2 ==str1[0:len(str2)])):   
                print("True\n"+"(***)")
                return True 
            #同一组相似字符表达在两组重复字符文本中均存在
            for k in range(len(arr[i])):
                if(k!=j):
                    if(str1.find(arr[i][j])==str2.find(arr[i][k]) and str1[:(str1.find(arr[i][j]))]==str2[:(str2.find(arr[i][k]))] and str1[(str1.find(arr[i][j])+len(arr[i][j])):]==str2[(str2.find(arr[i][k])+len(arr[i][k])):]):  
                        print(str1.find(arr[i][j]),str2.find(arr[i][k])) 
                        print(str1[:(str1.find(arr[i][j]))],str2[:(str2.find(arr[i][k]))])
                        print(str1[(str1.find(arr[i][j])+len(arr[i][j])):],str2[(str2.find(arr[i][k])+len(arr[i][k])):])
                        print("True\n"+arr[i][j]+" "+arr[i][k])
                        return True
                    #如果相似字符组中不存在两组重复文本
                    if(str1.find(arr[i][j])>=0 and  str1[:(str1.find(arr[i][j]))]==str2[:(str1.find(arr[i][j]))] and str1[(str1.find(arr[i][j])+len(arr[i][j])):]==str2[(str1.find(arr[i][j])+len(arr[i][j]))]):
                        str2.find(arr[i][k])==-1
                        print("True\n"+arr[i][j]+" "+str2[(str1.find(arr[i][j])):(str1.find(arr[i][j])+len(arr[i][j]))])
                        return True
                    if(str2.find(arr[i][j])>=0 and  str2[:(str2.find(arr[i][j]))]==str1[:(str2.find(arr[i][j]))] and str1[(str2.find(arr[i][j])+len(arr[i][j])):]==str2[(str2.find(arr[i][j])+len(arr[i][j])):]):
                        str1.find(arr[i][k])==-1
                        print("True\n"+str1[(str2.find(arr[i][j])):(str2.find(arr[i][j])+len(arr[i][j]))]+" "+arr[i][j])
                        return True
            #不同组的相似字符表达通过传递性将两组字符串中重复的文本中选出来
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i])):
                if(k!=j):
                    for l in range(len(arr) ):
                        if(l!=i):
                            for m in range(len(arr[l])):
                                for n in range(len(arr[l])):
                                    if(m != n):
                                        if(str1.find(arr[i][j])==str2.find(arr[l][m]) and str1[:(str1.find(arr[i][j]))]==str2[:(str2.find(arr[l][m]))] and str1[(str1.find(arr[i][j])+len(arr[i][j])):]==str2[(str2.find(arr[l][m])+len(arr[l][m])):]
                        and arr[i][k]==arr[l][n]):
                                            print(arr[i][k],arr[l][n])
                                            print(arr[i][j],arr[l][m])
                                            print("True\n"+arr[i][j]+" "+arr[l][m])
                                            return True

if __name__=="__main__":
    stringrepeat()
                





    
