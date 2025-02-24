"""
（a-i）用表示1-9，10*-26*表示j-z


"""
def decoder():
    lst = input().split("*")
    encoder=[]
    for i in range(len(lst)):
        if(len(lst[i])>2):
            for ele in lst[i][:-2]:
                encoder.append(ele)
            print(encoder)
            encoder.append(lst[i][-2:])
        if(len(lst[i])==2):
            encoder.append(lst[i])
    print(encoder)
    encoder = list(map(int,encoder))
    """
    将数字1-9 ,10-26分别映射为字母a-i,j-z
    """
    
    def number_to_letter(number):
        if(number<=9 and number>=1):
            return chr(ord("a")+number-1)
        if(number>=10 and number<=26):
            return chr(ord("j")+number-10)
    """
    将字母a-i,j-z分别映射为1-9 ，10-26
    """
    def letter_to_number(letter):
        if(letter>="a" and letter<="i"):
            return ord(letter)-ord("a")+1
        if(letter>="j" and letter<="z"):
            return ord(letter)-ord("j")+10
    letter_list=[]
    for j in range(len(encoder)):
        letter_list.append(number_to_letter(encoder[j]))
    print("letter_list",letter_list)
    string = "".join(letter_list)
    print(string)
    return string

    #mapper={1:"a",2:"b",3:"c",.....}
if __name__=="__main__":
    decoder()
    



    


