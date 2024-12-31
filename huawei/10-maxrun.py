"""
高效货运】

老李是货运公司承运人,老李的货车额定载货重量为wt。

现有两种货物,货物 A单件重量为wa,单件运费利润为pa,货物 B单件重量为wb,单件运费利润为pb,

老李每次发车时载货总重量刚好为货车额定的载货重量wt,车上必须同5时有货物A和货物B,货物A、B不可切割,

老李单车次满载运输可获得的最高利润是多少?


第一列输入是wa
第二列输入是wb
第三列输入是wt
第四列输入是pa
第五列输入是pb


"""

import math

s = input()
list = s.split(" ")
print(list)

m1 = math.floor(int(list[2]) / int(list[0]))
m2 = math.floor(int(list[2]) / int(list[1]))

for i in range(m1):
    for j in range(m2):
        if i * int(list[0]) + j * int(list[1]) == int(list[2]):
            print(max(i * int(list[3]) + j * int(list[4]), j * int(list[3]) + i * int(list[4])))
