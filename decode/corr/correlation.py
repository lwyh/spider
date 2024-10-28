import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(font="simhei")#遇到标签需要汉字的可以在绘图前加上这句
#设置随机种子
np.random.seed(42)
#数据量大小
data_size  = 100
#生成数据，确保'内力'和'武器熟练度'与’武功等级‘有较强的正相关
martial_arts_data = {
     '内力': np.random.randint(50, 150, size=data_size),
    '武器熟练度': np.random.randint(40, 100, size=data_size),
    '轻功': np.random.randint(30, 100, size=data_size),
    '外伤治愈能力': np.random.randint(20, 80, size=data_size),
}

martial_arts_df = pd.DataFrame(martial_arts_data)

#构建’武功等级‘,确保与"内力"和"武器熟练度"有较高的正相关性
martial_arts_df['武功等级'] = martial_arts_df['内力'] * 0.5 + martial_arts_df['武器熟练度'] * 0.3 + np.random.randint(0, 50, size=data_size)

#计算机相关系数
correlation_matrix = martial_arts_df.corr()

#使用seaborn绘制热力图，并显示相关系数值
plt.figure(figsize=(10,8))

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('武林高手属性与武功等级的相关性')
plt.show()

