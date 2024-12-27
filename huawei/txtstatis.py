"""

文本规则
1.文本以';'分隔，但空文本不能算语句
2.文本可以跨行，比如下面，是一条文本，而不是三条
3.文本可以支持字符串，‘，“,\"
4.支持注释，可以出现再字符串之外的任意位置，同窗以--开头，到换行结束
字符串内的--，不是注释

"""
def txtstatis():
    semicolon_count=0
    with open('D:\spider\huawei\example.txt', 'r', encoding='utf-8') as file: 
        file_iter=iter(file)
        while True:  
            try:  
                line=next(file_iter)
                print(line.strip())    
                semicolon_count +=line.count(';')
                line = file.readline()
            except StopIteration:
                print("line",line)
                semicolon_count +=1
                break
       
                
                    
            
    print(semicolon_count)



            
        



if __name__=='__main__':
    txtstatis()



