import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['STFangsong']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

# 设置组数、每组产品数量以及次品率的范围
num_groups = 100
num_products_per_group = 1000
min_defective_rate = 0.08
max_defective_rate = 0.2
d1=d2=0
# 生成每组的次品率
defective_rates = np.random.uniform(min_defective_rate, max_defective_rate, num_groups)

# 根据次品率生成每组产品的合格与次品标识
product_groups = [np.random.choice([0, 1], size=num_products_per_group, p=[1-rate, rate]) for rate in defective_rates]

# 创建一个Excel文件，并将每一组产品的数据存储到不同的表格中
with pd.ExcelWriter('product_data_separate_sheets.xlsx') as writer:
    for i, group in enumerate(product_groups):
        # 创建每一组的数据框
        df_group = pd.DataFrame({
            'Product_Status': group,
            'Defective_Rate': defective_rates[i]
        })
        # 将该组数据写入单独的sheet
        df_group.to_excel(writer, sheet_name=f'Group_{i + 1}', index=False)

print("Excel文件已生成，文件名为: product_data_separate_sheets.xlsx")
# 绘制次品率折线图
groups = list(range(1, 101))
plt.figure(figsize=(10, 6))
plt.bar(groups, defective_rates, color='b', label='次品率')

# 添加标题和标签
plt.title('随机生成100组样本的次品率分布')
plt.xlabel('组别')
plt.ylabel('次品率')
plt.grid(True)
plt.legend()

# 显示图形
plt.show()
