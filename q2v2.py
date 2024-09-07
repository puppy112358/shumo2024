# 导入库
import numpy as np


#遍历算法

# 定义情境数据，用于存储每个情境的相关参数
class Qingjing:
    def __init__(self, cipin_rate1, goumai_1, jiance_1,
                 cipin_rate2, goumai_2, jiance_2,
                 chengpin_cipin_rate, zhuangpei, chengpin_jiance,
                 shoujia, sunshi_tuihuan, chaijie_cost):
        # 初始化零配件1的次品率、购买单价、检测成本
        self.part1_def_rate = cipin_rate1
        self.part1_price = goumai_1
        self.part1_det_cost = jiance_1

        # 初始化零配件2的次品率、购买单价、检测成本
        self.part2_def_rate = cipin_rate2
        self.part2_price = goumai_2
        self.part2_det_cost = jiance_2

        # 初始化成品的次品率、装配成本、检测成本
        self.product_def_rate = chengpin_cipin_rate
        self.assembly_cost = zhuangpei
        self.product_det_cost = chengpin_jiance

        # 初始化市场售价、退换损失、拆解费用
        self.market_price = shoujia
        self.return_loss = sunshi_tuihuan
        self.disassembly_cost = chaijie_cost


# 检测零配件
# return :数量，次品率，成本
def detect_lingjian(jiance_, cipin_rate, jiance_cost):
    # 若不检测零配件，次品率带来的损失
    if jiance_ == 1:  #检测
        print('检测')
        loss = jiance_cost
        cipin_rate = 0
        num_lingjian = 1 - cipin_rate
    else:
        loss = 0
        num_lingjian = 1
    # 若损失大于检测成本，进行检测
    return num_lingjian,cipin_rate,loss


# 检测成品
def detect_chanpin(num_lingjian1,num_lingjian2,cipin_rate, jian_cost, tuihuan_loss):
    loss = cipin_rate * tuihuan_loss
    return loss > jian_cost


# 计算是否拆解
def disassemble(disassembly_cost, def_rate, return_loss):
    # 期望损失
    expected_loss = def_rate * return_loss
    return expected_loss > disassembly_cost


# 主函数，处理每种情境
def juece(qingjing):
    # 1. 零配件检测决策
    detect_lingjian1 = detect_lingjian(qingjing.part1_def_rate, qingjing.part1_det_cost, qingjing.assembly_cost)
    detect_lingjian2 = detect_lingjian(qingjing.part2_def_rate, qingjing.part2_det_cost, qingjing.assembly_cost)
    print(f"零配件1检测：{'是' if detect_lingjian1 else '否'}")
    print(f"零配件2检测：{'是' if detect_lingjian2 else '否'}")

    # 2. 成品检测决策
    detect_chenpin = detect_chanpin(qingjing.product_def_rate, qingjing.product_det_cost, qingjing.return_loss)
    print(f"成品检测：{'是' if detect_chenpin else '否'}")

    # 3. 拆解决策
    chanjie_chanpin = disassemble(qingjing.disassembly_cost, qingjing.product_def_rate, qingjing.return_loss)
    print(f"不合格成品拆解：{'是' if chanjie_chanpin else '否'}")


# 定义6个情境，基于表 1 的数据
scenarios = [
    # 情境1的参数
    Qingjing(0.1, 4, 2, 0.1, 18, 3, 0.1, 6, 3, 56, 6, 5),
    # 情境2的参数
    Qingjing(0.2, 4, 2, 0.2, 18, 3, 0.2, 6, 3, 56, 6, 5),
    # 情境3的参数
    Qingjing(0.1, 4, 2, 0.1, 18, 3, 0.1, 6, 30, 56, 30, 5),
    # 情境4的参数
    Qingjing(0.2, 4, 1, 0.2, 18, 1, 0.2, 6, 2, 56, 30, 5),
    # 情境5的参数
    Qingjing(0.1, 4, 8, 0.2, 18, 1, 0.1, 6, 2, 56, 10, 5),
    # 情境6的参数
    Qingjing(0.05, 4, 2, 0.05, 18, 3, 0.05, 6, 3, 56, 10, 40),
]

# 处理每个情境并输出结果
for i, changjing in enumerate(scenarios):
    print(f"情境 {i + 1}:")
    juece(changjing)  # 对每个情境进行处理
    print("\n")  # 换行区分每个情境的输出
