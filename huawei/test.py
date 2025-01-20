import random

def random_distribute_items(m, n):
    items = list(range(n))  # 创建物品列表
    print(items,"items")
    random.shuffle(items)  # 随机打乱顺序
    distribution = [[] for _ in range(m)]  # 创建m个空列表用于存储分配结果
    for i, item in enumerate(items):
        distribution[i % m].append(item)  # 分配物品
    return distribution

# 示例
m = 5  # 人数
n = 23  # 物品数
result = random_distribute_items(m, n)
for i, group in enumerate(result):
    print(f"Person {i+1} gets: {group}")