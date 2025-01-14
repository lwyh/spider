def remove_last_two_slashes_and_content(s):
    # 从右侧开始分割最后两个'/'，最大分割次数为2
    #parts = s.rsplit('/', 2)
    # 重新组合剩余的部分，排除最后两个'/'及其之间的内容
    #path = "/path/to/some/deeply/nested/"
    parts2 = s.rsplit('/', 2)
    new_path = '/'.join(parts2[:-2]) + '/'  if len(parts2) > 2 else parts2[0]
    print(new_path)
    return new_path
    
if __name__=="__main__":
    string=input()
    remove_last_two_slashes_and_content(string)