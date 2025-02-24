"""
英文输入法
"""
import re
def wordextend():
    str1=input() 
    str2=input()
    delimiter=r"[ '.,]"
    kuda = re.split(delimiter,str1)
    kuda = [ele for ele in kuda if ele]
    print(kuda)
    extend_list=[]
    
    for substring in kuda:
        #注意此处的子串不是包含str2,而是要等于str2
        if any(substring[:i]==str2  for i in range(1,len(substring))):
            extend_list.append(substring)
    #print(extend_list,"extend_list")
    out=""
    if(extend_list==[]):
        print(str2)
    else:
        out = " ".join(extend_list)
        print(out)
    return out

if __name__=="__main__":
    wordextend()
            
    






