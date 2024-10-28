##坐标移动
#A  向左 D 向右  W 向上 S 向下

import sys


a = input().split(";")
location = [0,0]
steps = 0
dir = ["A","S","D","W"]
for item in a: 
    #第一种情况，没有3个字符
    if len(item)<2:
        continue
    new_string = item[1:]
    #第二种情况，不是以ASDW开头的字符串
    if item[0] not in dir:
        continue
    #第三种情况，不是纯数字，为负数或者其他非数字
    if(not new_string.isdigit()) or (int(new_string)<0):
        continue
    steps = int(new_string)
    if item[0] == "A":
        location[0] = location[0]-steps
    if item[0] == "D":
        location[0] = location[0]+steps
    if item[0] == "S":
        location[1] = location[1]-steps
    if item[0] == "W":
        location[1] = location[1]+steps
print(location[0],location[1],sep=",")