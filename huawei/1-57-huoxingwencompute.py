"""
火星人运算符
x#y=4*x+3*y+2
x$y=2*x+y+3




# n>=0 and n<=4294967295
本题的逻辑并不复杂，但是分类讨论的情况比较多

"""
import re
def huoxingwencompute():
    ss=input()
    delimiter=r'[#\s$]+'
    result = re.split(delimiter,ss)
    print("result",result)
    if(ss.count("+")>0 or ss.count("-")>0 or ss.count("*")>0 or ss.count("/")>0 
    or  ss.startswith("#") or ss.startswith("$") or ss.endswith("#") or ss.endswith("$")
    or ss.count("#$")>0 or ss.count("$#")>0
    or ss.count(" ")>0 ):
        return -1 
    elif any(int(ele)>4294967295  or int(ele)<0 for ele in result):
        return -1
    else:
        if(ss.count("#")>0 and ss.count("$")>0):
            lst1=ss.split("$")
            first_list=[]
            lst2=[]
            for ele in lst1:  
                lst2=ele.split("#")
                print(lst2)
                x=int(lst2[0])
                y=int(lst2[1])
                first_list.append(4*x+3*y+2)
            print("first_list",first_list)
            x=first_list[0]
            y=first_list[1]
            for j in range(len(first_list)-1):
                if(len(first_list)==2):
                    break
                else:
                    if(j+1!=len(first_list)-1):
                        x=2*x+y+3
                        y=first_list[j+2]
                        print("x,y",x,y)
            print("xx,yy",x,y)
            x=2*x+y+3 
            print(x)
            return x
            
        if(ss.count("#")>0 and ss.count("$")==0):
            first_list=list(map(int,ss.split("#")))
            x=first_list[0]
            y=first_list[1]
            for j in range(len(first_list)-1):
                if(len(first_list)==2):
                    break
                else:
                    if(j+1!=len(first_list)-1):
                        x=4*x+3*y+2
                        y=first_list[j+2]
                        print("x,y",x,y)
            print("xx,yy",x,y)
            x=4*x+3*y+2
            print(x)
            return x

        if(ss.count("$")>0 and ss.count("#")==0):
            first_list=list(map(int,ss.split("$")))
            x=first_list[0]
            y=first_list[1]
            for j in range(len(first_list)-1):
                if(len(first_list)==2):
                    break
                else:
                    if(j+1!=len(first_list)-1):
                        x=2*x+y+3
                        y=first_list[j+2]
                        print("x,y",x,y)
            print("xx,yy",x,y)
            x=2*x+y+3
            print(x)
            return x
            
        
if __name__=="__main__":
    huoxingwencompute()

            



        



