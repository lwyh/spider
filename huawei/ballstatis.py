import pandas as pd

# 读取Excel文件
df = pd.read_excel('D:\spider\huawei\老铁队外战数据榜.xlsx')

# 使用0替换NaN值
df.fillna(0, inplace=True)

# 将进球和助攻列转换为整数
df['进球'] = df['进球'].astype(int)
df['助攻'] = df['助攻'].astype(int)

# 按球员姓名分组，并计算总进球数和助攻数
player_stats = df.groupby('姓名')[['进球', '助攻']].sum().reset_index()

# 按照进球数和助攻数排序
player_stats = player_stats.sort_values(by=['进球', '助攻'], ascending=[False, False])

# 输出每个球员的总进球数和助攻数
print(player_stats)
# 输出每个球员的总进球数和助攻数到Excel文件
player_stats.to_excel('球员进球助攻统计.xlsx', index=False)