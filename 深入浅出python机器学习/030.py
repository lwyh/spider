import pandas as pd
import numpy as np
import os
import random


#定义文本数据文件的额存储路径
data_folder = 'D:\\stock_database\\aclImdb_v1\\aclImdb\\train\\neg'
#获取文件夹中所有文本文件的列表
file_list = [f for f in os.listdir(data_folder) if f.endswith('.txt')]
#确保文件数量足够
assert len(file_list) >=50,"Not enough text files in the folder."
#随机抽取50个文件
random.seed(42)
selected_files = random.sample(file_list,50)

#读取并处理这些文件的内容
selected_texts = []
for file_name in selected_files:
    file_path = os.path.join(data_folder,file_name)
    with open(file_path,'r',encoding='utf-8') as file:
        content = file.read()
        selected_texts.append(content)


for i, text in enumerate(selected_texts, 1):
    print(f"Text {i}:")






# 将训练集和测试集合并为一个大的数据集
