"""
石头剪刀布游戏，ABC分别代表石头，剪刀，布
只出现ABC中的其中两种，则有赢家出现
只出现ABC中的一种，平局
同时出现ABC三种，也判平局

输出赢家ID,平局时输出null
不确定输入的行数时，可以将整个输入作为一个字符串，然后再按照不同规则切分
"""
import sys
def RockPaperScissors():
    players=dict()
    while True:
        line = input()
        lst=line.split()
        #玩家id只包含英文字母和数字
        if(len(lst)>0 and lst[0].isalnum()):
            players[lst[0]]=lst[1]
        if line.strip()=="":
            break
    print(players,"players")
    #平局情况列举
    if(list(players.values()).count("A")>0 and 
     list(players.values()).count("B")>0 and 
     list(players.values()).count("C")>0 or
     (len(set(players.values())))==1):
     print("NULL")
     return -1
    else:
        #赢家情况出现
        if(len(set(players.values()))==2
        and list(players.values()).count("A")==0):
            player=[key for key,value in players.items() if value=="B"]
            sorted_player=sorted(player)
            for id in sorted_player:
                print(id)
        if(len(set(players.values()))==2
        and list(players.values()).count("B")==0):
            player=[key for key,value in players.items() if value=="C"]
            sorted_player=sorted(player)
            for id in sorted_player:
                print(id)
        if(len(set(players.values()))==2
        and list(players.values()).count("C")==0):
            player=[key for key,value in players.items() if value=="A"]
            sorted_player=sorted(player)
            for id in sorted_player:
                print(id)
        return 0


if __name__=="__main__":
    RockPaperScissors()
