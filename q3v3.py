# 导入库
import numpy as np

# 拆解权重
chaijie_q = 0.3
loss_ = []


# 定义情境数据
class Qingjing:
    def __init__(self, cipin_rate1, goumai_1, jiance_1,
                 cipin_rate2, goumai_2, jiance_2,
                 chengpin_cipin_rate, zhuangpei, chengpin_jiance,
                 shoujia, sunshi_tuihuan, chaijie_cost):
        # 零配件1
        self.part1_def_rate = cipin_rate1
        self.part1_price = goumai_1
        self.part1_det_cost = jiance_1

        # 零配件2
        self.part2_def_rate = cipin_rate2
        self.part2_price = goumai_2
        self.part2_det_cost = jiance_2

        # 成品
        self.product_def_rate = chengpin_cipin_rate
        self.assembly_cost = zhuangpei
        self.product_det_cost = chengpin_jiance

        self.market_price = shoujia
        self.return_loss = sunshi_tuihuan
        self.disassembly_cost = chaijie_cost


# 步骤一，购买零件,并组装
def buy_part(choose, part_def_rate, part_price, part_det_cost):
    # 不检测直接组装
    if choose == 0:
        # print('不检测：')
        price0 = part_price
        # print('过程成本:', price0)
        return price0, part_def_rate
    else:
        # 检测
        # print('检测：')
        price1 = part_def_rate * part_price + part_det_cost
        part_def_rate = 0.0
        # print('过程成本:', price1)
        return price1, part_def_rate
    # 步骤2，是否检测成品并销售


def detect_product(choose, def_product_rate, part_def_rate,
                   part_value, loss_return, jian_cost, sale_):
    profit = 0
    def_rate = 1 - (1 - def_product_rate) * (1 - part_def_rate[0]) * (1 - part_def_rate[1])
    if choose == 0:
        # print('不检测：')
        # def_rate = 1 - (1-def_product_rate)*(1-part_def_rate[0])*(1-part_def_rate[1])
        profit = sale_ - loss_return * def_rate - part_value[0] - part_def_rate[1]
    else:
        # print('检测：')
        profit = sale_ - jian_cost
    # print('利润:', profit)
    return profit, def_rate


# 步骤三，是否拆解
def disassemble(choose, disassembly_cost, def_num, part_value):
    # 不拆
    loss = 0
    if choose == 1:
        # print('不拆解')
        # print('损失:', loss)
    # else:
        # print('拆解')
        loss = (disassembly_cost - (part_value[0] + part_value[1]) * 0.4) * def_num
        # print('损失:', loss)
    return loss


# # 检测零配件
# # return :数量，次品率
# def detect_lingjian(cipin_rate, jiance_cost, zuzhuang_cost, chengben_lingjian):
#     cipin_num = 1
#     # 若不检测零配件，次品率带来的损失
#     print('不检测：')
#     loss = cipin_rate * (zuzhuang_cost + chengben_lingjian)
#     # 若损失大于检测成本，进行检测
#     if loss > jiance_cost:
#         cipin_num = 1 - cipin_rate
#         cipin_rate = 0.0
#         loss_all = loss
#         print('检测')
#     else:
#         print('不检测')
#         loss_all = jiance_cost + cipin_rate
#     return cipin_rate, cipin_num, loss_all
#
#
# # 检测成品
# def detect_chanpin(cipin_rate, chengpin_cipin, tuihuo, jian_cost, chaijie):
#     # 不检测
#     cipin_num = 0
#     loss = (1 - (1 - cipin_rate[0]) * (1 - cipin_rate[1]) * (1 - chengpin_cipin)) * (tuihuo + chaijie * chaijie_q)
#     if loss > jian_cost:  # 检测
#         cipin_num = 1 - (1 - cipin_rate[0]) * (1 - cipin_rate[1]) * (1 - chengpin_cipin)  # 次品'
#         chengpin_cipin = 0.0
#         loss_all = loss
#         print('检测成品')
#     else:
#         print('不检测成品')
#         loss_all = jian_cost
#     return chengpin_cipin, cipin_num, loss_all
#
#
# # 拆解
# def disassemble(cipin_num, disassembly_cost, tuihuo, lingjian_1, lingjian_2):
#     # 不拆
#     # cipin_value = ((1 - cipin_rate[0]) * (1 - cipin_rate[1]) *cipin_chengpin* (lingjian_1 + lingjian_2) + (1 - cipin_rate[0]) *
#     #                cipin_rate[1] * lingjian_1 + cipin_rate[0] * (1 - cipin_rate[1]) * lingjian_2) / (
#     #     (1-cipin_rate[0]) +(1-cipin_rate[1])*cipin_chengpin+(1-cipin_rate[0])*cipin_rate[1]+cipin_rate[0]*(1-cipin_rate[1]) )
#     cipin_value = (lingjian_1 + lingjian_2) / 3
#     loss = cipin_num * tuihuo + cipin_value
#     if loss > disassembly_cost:
#         print('拆解')
#         loss_all = loss
#     else:
#         print('不拆解')
#         loss_all = disassembly_cost
#     return loss_all
#
#
# 遍历

def Traverse(qingjing):
    loss_least = 1000
    # 1. 零配件检测决策
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    loss_ = 0
                    print(f"零配件1：检测{i}, 零配件2：检测{j}, 成品：检测{k}，拆解{l}")
                    price0, part1_def_rate = buy_part(i, qingjing.part1_def_rate, qingjing.part1_price,
                                                      qingjing.part1_det_cost)
                    price1, part2_def_rate = buy_part(j, qingjing.part2_def_rate, qingjing.part2_price,
                                                      qingjing.part2_det_cost)
                    part_value = [price0, price1]
                    loss_ = price0 + price1
                    # 2. 成品检测决策
                    profit, def_rate = detect_product(k, qingjing.product_def_rate, [part1_def_rate, part2_def_rate],
                                                      part_value, qingjing.return_loss, qingjing.product_det_cost,
                                                      qingjing.market_price)
                    loss_ = loss_ - profit
                    # 3. 拆解决策
                    loss = disassemble(l, qingjing.disassembly_cost, def_rate, part_value)
                    loss_ = loss_ + loss
                    print('总损失：', loss_)
                    if loss_ < loss_least:
                        loss_least = loss_
                    print('最小损失：', loss_least)


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
    Traverse(changjing)  # 对每个情境进行处理
    print("\n")  # 换行区分每个情境的输出
