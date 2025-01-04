import re
from collections import Counter



# 假设这是文本内容

# 打开文件，使用with语句可以确保文件在使用后自动关闭
with open(r'D:\spider\huawei\2024快乐老铁队报名表.txt', 'r', encoding='utf-8') as file:
    # 读取文件的全部内容
    content = file.read()

# 打印文件内容
#print(content)




# 使用正则表达式匹配人名
# 正则表达式解释：
# \d+ 匹配一个或多个数字
# \. 匹配点号
# \s+ 匹配一个或多个空白字符
# ([\u4e00-\u9fffA-Za-z]+) 匹配一个或多个汉字或英文字符
pattern = r'\d+\.\s+([\u4e00-\u9fffA-Za-z]+)'

# 查找所有匹配的人名
matches = re.findall(pattern, content)

# 打印匹配到的人名
for match in matches:
    print(match)

name_counts = Counter()
for name in matches:
    # 使用正则表达式匹配人名，忽略大小写
    names = re.findall(r'\b' + re.escape(name) + r'\b', content, re.IGNORECASE)
    name_counts[name] = len(names)

# 打印结果


# 定义一个映射字典，将一些人名映射为同一个键
remap = {'z': '周志', '坚决二过一': '王佳欣', 'mq梦麒': '张梦麒',
         'Lang': '吴浪', '尧': '胡新尧', '邓sir': '邓进华',
         'zz': '周志', '平': '周平', '代平哥': '周平',
        '爱思唯尔珠宝': '珠宝哥', '一碗木瓜水': '钟斌',
        '伟哥': '李伟', '超能能': '超哥', '贾超': '超哥', 
         '谢律': '谢道铕', 'CozyP': '高子鹏'}

# 创建一个新的字典来存储合并后的结果
merged_dict = {}
mapped_key=''
# 遍历原始字典，根据映射字典更新键并合并值
for name, value in name_counts.items():
    if name in remap.keys():
        mapped_key = remap[name]
        if mapped_key in merged_dict:
            merged_dict[mapped_key] += value
        else:
            merged_dict[mapped_key] = value
    else:
        merged_dict[name]=value
    

    

# 打印合并后的字典
print(merged_dict)

sorted_dict = dict(sorted(merged_dict.items(), key=lambda item: item[1], reverse=True))
for name, count in sorted_dict.items():
    print(f"{name}: {count}")