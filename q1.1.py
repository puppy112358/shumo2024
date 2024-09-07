# 只包含一组数据
import numpy as np
import pandas as pd
import random
from scipy.stats import binom
import matplotlib.pyplot as plt
from scipy.stats import norm

# 设置参数
total_products = 1000  # 产品总数
defect_rate = 0.1  # 次品率
# 初始化结果
decisions = []  # 最终决策 (0: 接收, 1: 拒收)
# # # 随机生成产品是否为次品的标签
# # # 1 代表次品，0 代表合格品
# data = np.random.choice([0, 1], size=total_products, p=[1 - defect_rate, defect_rate])
# #
# # # 创建一个数据框用于存储数据
# df = pd.DataFrame(data, columns=['Defect'])
#
# # # 打印前几行数据查看结果
# # print(df.head())
#
# # 保存到 CSV 文件
# df.to_csv('product_defects.csv', index=False)
plt.rcParams['font.sans-serif'] = ['STFangsong']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

# 加载数据集
# with pd.ExcelWriter('binomial_double_sampling_decisions.xlsx') as writer:
for j in range(0, 99):
    cipin_num1 = cipin_num2 = 0
    df = pd.read_excel('product_data_separate_sheets.xlsx', sheet_name=f'Group_{j + 1}', index_col=False)

    # 参数设定
    all_1 = 20  # 第一次抽样数量
    all_2 = 30  # 第二次抽样数量
    c1 = 5  # 第一次抽样接受临界值
    c2 = 10  # 第一次抽样拒收临界值
    p = 0.10  # 设定的次品率
    alpha = 0.05  # 95% 置信区间对应的 alpha 值

    # 计算在次品率 p 下，95% 置信区间内的次品数量范围
    accept_limit_first = binom.ppf(1 - alpha, all_1, p)  # 第一次抽样接受的最大次品数
    accept_limit_total = binom.ppf(1 - alpha, all_1 + all_2, p)  # 总样本接受的最大次品数
    # dff =
    # 模拟双重抽样过程
    for i in range(0, all_1):  #随机抽n1个
        # 第一次抽样次品数
        sample_1 = df['Product_Status'].iloc[random.randint(0, 500)]
        cipin_num1 = cipin_num1 + sample_1  # 第一次抽样次品数
        # 判断第一次抽样结果
    percent_second = cipin_num1 / all_1
    # 计算检验统计量 Z
    Z = (percent_second - p) / np.sqrt((p * (1 - p)) / all_1)
    Z_critical = norm.ppf(1 - alpha / 2)  # 双尾检验，查标准正态分布表
    # 检验结果
    if cipin_num1 > accept_limit_first:
        print("次品太多")
        decisions.append(1)  # 拒绝
    else:
        # print("拒绝原假设，样本次品率与假设次品率没有显著差异。")
        # if d1 < c1 or d1 <= accept_limit_first:  # 小于接受临界值或在接受概率区间内
        #     decisions.append(0)  # 接收
        # elif d1 > c2:  # 大于拒收临界值
        #     decisions.append(1)  # 拒收
        # else:
        # 进行第二次抽样
        for k in range(0, all_2):
            second_sample = df['Product_Status'].iloc[random.randint(500, 800)]
            cipin_num2 = cipin_num2 + second_sample  # 第二次抽样次品数

        # 总次品数
        total_cipin = cipin_num1 + cipin_num2

        percent_second = total_cipin / (all_1 + all_2)
        # 计算检验统计量 Z
        Z = (percent_second - p) / np.sqrt((p * (1 - p)) / (all_1 + all_2))
        Z_critical = norm.ppf(1 - alpha / 2)  # 双尾检验，查标准正态分布表
        # 检验结果
        if abs(Z) < Z_critical:
            print("样本次品率与假设次品率无显著差异。")
            decisions.append(0)  # 接收
        elif percent_second < p:
            print("样本次品率与假设次品率有显著差异，但是次品数量偏少")
            decisions.append(0)  # 接收
        else:
            print("拒绝原假设")
            decisions.append(1)  # 接收
groups = list(range(0, 99))
plt.figure(figsize=(10, 6))
plt.plot(groups, decisions, 'o', color='b', label='是否拒收')

# 添加标题和标签
plt.title('100组随机样本抽样检测结果')
plt.xlabel('组别')
plt.ylabel('是否拒收')
plt.grid(True)
plt.legend()

# 显示图形
plt.show()
