"""
模拟目录管理，输入一系列命令序列，输出最后一个命令输出执行的结果
约束：
1.判断目录是否重名
2.判断目录名是否正确，只支持小写字母，不支持嵌套路径和绝对路径
3.pwd输出当前的绝对路径
4.目录符号为/,根目录是/作为初始目录
5.支持的命令包括mkdir,cd,pwd

"""
def directorys():
    commands=[]
    N=int(input())
    for i in range(N):
        commands.append(list(input().split()))
    print(commands)
    directory_name=[]
    
    
    def is_valid_command(command):
        if (command.isalpha() and command.islower()):
        # 检查命令字符串中是否包含 '/'
            if ("/" in command):
                return False

        # 检查命令字符串是否以 '/' 开头
            if (command.startswith("/")):
                return False
    
        return True
    def remove_last_two_slashes_and_content(s):
    # 从右侧开始分割最后两个'/'，最大分割次数为2
    #parts = s.rsplit('/', 2)
    # 重新组合剩余的部分，排除最后两个'/'及其之间的内容
    #path = "/path/to/some/deeply/nested/"
        parts2 = s.rsplit('/', 2)
        new_path = '/'.join(parts2[:-2]) + '/'  if len(parts2) > 2 else parts2[0]
        print(new_path)
        return new_path
    #本题的关键是current_directory需要作为变量进行更新
    def outputcommand(commands,index,current_directory):
        directory=''
        #将mkdir中不在目录中且符合约束条件的添加进去
        if((index<len(commands) and commands[index][0]=='mkdir' and  is_valid_command(commands[index][1])    and commands[index][1] not in directory_name)  ):
            directory_name.append(commands[index][1])
            return current_directory
        #将mkdir中目录名重复或者不符合约束条件的去掉
        if((index<len(commands) and commands[index][0]=='mkdir' and commands[index][1]  in directory_name) or  (index<len(commands) and commands[index][0]=='mkdir' and not is_valid_command)):
            return 
        #将cd 中目录名是否正确已经存在
        if(index<len(commands) and commands[index][0]=='cd' and is_valid_command(commands[index][1]) and commands[index][1] in directory_name):
            directory=commands[index][1]
            print(directory)
            print("current_directory0",current_directory)
            current_directory=f"{current_directory}{directory}/"
            print("current_directory1",current_directory)
            return current_directory
        #cd ../中的操作单独做处理
        if(index<len(commands) and commands[index][0]=='cd' and  commands[index][1] == '../'):
            if(current_directory=='/'):
                return current_directory
            else:
                current_directory=remove_last_two_slashes_and_content(current_directory)
                return current_directory
        #将cd 中目录名不存在或者不符合约束条件的去掉
        if((index<len(commands) and commands[index][0]=='cd' and commands[index][1]  not in directory_name) or (index<len(commands) and commands[index][0]=='cd' and is_valid_command(commands[index][1]))):
            return
        #处理pwd结果
        if(index<len(commands) and commands[index][0]=='pwd'):
            print(current_directory)
            return current_directory


    current_directory='/'      
    for j in range(len(commands)):
        current_directory = outputcommand(commands,j,current_directory)

    print(current_directory)
    return current_directory


 

if __name__=="__main__":
    directorys()