import numpy as np
import pandas as pd
from scipy.stats import binom

# 设置参数
total_products = 10000  # 产品总数
defect_rate = 0.09  # 次品率

# 随机生成产品是否为次品的标签
# 1 代表次品，0 代表合格品
data = np.random.choice([0, 1], size=total_products, p=[1 - defect_rate, defect_rate])

# 创建一个数据框用于存储数据
df = pd.DataFrame(data, columns=['Defect'])

# # 打印前几行数据查看结果
# print(df.head())

# 保存到 CSV 文件
df.to_csv('product_defects.csv', index=False)

# 加载数据集
df = pd.read_csv('product_defects.csv')

# 参数设定
n1 = 20  # 第一次抽样数量
n2 = 30  # 第二次抽样数量
c1 = 2   # 第一次抽样接受临界值
c2 = 5   # 第一次抽样拒收临界值
p = 0.10  # 设定的次品率
alpha = 0.05  # 95% 置信区间对应的 alpha 值

# 初始化结果
decisions = []  # 最终决策 (0: 接收, 1: 拒收)

# 计算在次品率 p 下，95% 置信区间内的次品数量范围
accept_limit_first = binom.ppf(1 - alpha, n1, p)  # 第一次抽样接受的最大次品数
accept_limit_total = binom.ppf(1 - alpha, n1 + n2, p)  # 总样本接受的最大次品数

# 模拟双重抽样过程
for i in range(0, len(df), n1 + n2):
    # 第一次抽样次品数
    first_sample = df['Defect'].iloc[i:i + n1].values
    d1 = np.sum(first_sample)  # 第一次抽样次品数

    # 判断第一次抽样结果
    if d1 < c1 or d1 <= accept_limit_first:  # 小于接受临界值或在接受概率区间内
        decisions.append(0)  # 接收
    elif d1 > c2:  # 大于拒收临界值
        decisions.append(1)  # 拒收
    else:
        # 进行第二次抽样
        second_sample = df['Defect'].iloc[i + n1:i + n1 + n2].values
        d2 = np.sum(second_sample)  # 第二次抽样次品数

        # 总次品数
        total_defects = d1 + d2

        # 根据总次品数判断
        if total_defects <= accept_limit_total:  # 总次品数在可接受范围内
            decisions.append(0)  # 接收
        else:
            decisions.append(1)  # 拒收

# 将决策结果添加到数据集中
df['Decision'] = pd.Series(decisions).repeat(n1 + n2).reset_index(drop=True)

# 查看前几行结果
print(df.head(30))
print(decisions)
# 保存结果到 CSV 文件
df.to_csv('binomial_double_sampling_decisions.csv', index=False)
