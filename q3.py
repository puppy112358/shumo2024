
# 导入库
import numpy as np

#拆解权重
chaijie_q = 0.3
# 定义情境数据
class Qingjing:
    def __init__(self, cipin_rate1, goumai_1, jiance_1,
                 cipin_rate2, goumai_2, jiance_2,
                 cipin_rate3, goumai_3, jiance_3,
                 cipin_rate4, goumai_4, jiance_4,
                 cipin_rate5, goumai_5, jiance_5,
                 cipin_rate6, goumai_6, jiance_6,
                 cipin_rate7, goumai_7, jiance_7,
                 cipin_rate8, goumai_8, jiance_8,
                 banchengpin_cipin_rate, banzhuangpei, banchengpin_jiance, banchaijie_cost,
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
        # 零配件3
        self.part3_def_rate = cipin_rate3
        self.part3_price = goumai_3
        self.part3_det_cost = jiance_3
        # 零配件4
        self.part4_def_rate = cipin_rate4
        self.part4_price = goumai_4
        self.part4_det_cost = jiance_4
        # 零配件5
        self.part5_def_rate = cipin_rate5
        self.part5_price = goumai_5
        self.part5_det_cost = jiance_5
        # 零配件6
        self.part6_def_rate = cipin_rate6
        self.part6_price = goumai_6
        self.part6_det_cost = jiance_6
        # 零配件7
        self.part7_def_rate = cipin_rate7
        self.part7_price = goumai_7
        self.part7_det_cost = jiance_7
        # 零配件8
        self.part8_def_rate = cipin_rate8
        self.part8_price = goumai_8
        self.part8_det_cost = jiance_8

        # 半成品
        self.product_def_rate = chengpin_cipin_rate
        self.assembly_cost = zhuangpei
        self.product_det_cost = chengpin_jiance

        self.market_price = shoujia
        self.return_loss = sunshi_tuihuan
        self.disassembly_cost = chaijie_cost
        # 成品
        self.product_def_rate = chengpin_cipin_rate
        self.assembly_cost = zhuangpei
        self.product_det_cost = chengpin_jiance

        self.market_price = shoujia
        self.return_loss = sunshi_tuihuan
        self.disassembly_cost = chaijie_cost


# 检测零配件
# return :数量，次品率
def detect_lingjian(cipin_rate, jiance_cost, zuzhuang_cost, chengben_lingjian):
    cipin_num = 1
    # 若不检测零配件，次品率带来的损失
    loss = cipin_rate * (zuzhuang_cost + chengben_lingjian)
    # 若损失大于检测成本，进行检测
    if loss > jiance_cost + cipin_rate :
        cipin_num = 1 - cipin_rate
        cipin_rate = 0.0
        print('检测')
    else:
        print('不检测')
    return cipin_rate, cipin_num


# 检测成品
def detect_chanpin(cipin_rate, chengpin_cipin, tuihuo, jian_cost, chaijie):
    #不检测
    cipin_num = 0
    loss = (1 - (1 - cipin_rate[0]) * (1 - cipin_rate[1]) * (1 - chengpin_cipin)) * (tuihuo + chaijie * chaijie_q)
    if loss > jian_cost:  #检测
        cipin_num = 1 - (1 - cipin_rate[0]) * (1 - cipin_rate[1]) * (1 - chengpin_cipin)  #次品'
        chengpin_cipin = 0.0
        print('检测成品')
    else:
        print('不检测成品')
    return chengpin_cipin, cipin_num


# 拆解
def disassemble(cipin_rate, cipin_num, disassembly_cost, tuihuo, lingjian_1, lingjian_2):
    # 不拆
    # cipin_value = ((1 - cipin_rate[0]) * (1 - cipin_rate[1]) *cipin_chengpin* (lingjian_1 + lingjian_2) + (1 - cipin_rate[0]) *
    #                cipin_rate[1] * lingjian_1 + cipin_rate[0] * (1 - cipin_rate[1]) * lingjian_2) / (
    #     (1-cipin_rate[0]) +(1-cipin_rate[1])*cipin_chengpin+(1-cipin_rate[0])*cipin_rate[1]+cipin_rate[0]*(1-cipin_rate[1]) )
    cipin_value = (lingjian_1+lingjian_2)/3
    loss = cipin_num * tuihuo + cipin_value
    if loss > disassembly_cost:
        print('拆解')
    else:
        print('不拆解')
        return loss


# 主函数，处理每种情境
def juece(qingjing):
    # 1. 零配件检测决策
    rate_lingjian1, lingjian1_num = detect_lingjian(qingjing.part1_def_rate, qingjing.part1_det_cost,
                                                    qingjing.assembly_cost,
                                                    qingjing.part1_price)
    rate_lingjian2, lingjian2_num = detect_lingjian(qingjing.part2_def_rate, qingjing.part2_det_cost,
                                                    qingjing.assembly_cost,
                                                    qingjing.market_price)
    rate_lingjian3, lingjian3_num = detect_lingjian(qingjing.part1_def_rate, qingjing.part1_det_cost,
                                                    qingjing.assembly_cost,
                                                    qingjing.market_price)
    rate_lingjian4, lingjian4_num = detect_lingjian(qingjing.part2_def_rate, qingjing.part2_det_cost,
                                                    qingjing.assembly_cost,
                                                    qingjing.market_price)
    rate_lingjian5, lingjian5_num = detect_lingjian(qingjing.part1_def_rate, qingjing.part1_det_cost,
                                                    qingjing.assembly_cost,
                                                    qingjing.market_price)
    rate_lingjian6, lingjian6_num = detect_lingjian(qingjing.part2_def_rate, qingjing.part2_det_cost,
                                                    qingjing.assembly_cost,
                                                    qingjing.market_price)
    rate_lingjian7, lingjian7_num = detect_lingjian(qingjing.part1_def_rate, qingjing.part1_det_cost,
                                                    qingjing.assembly_cost,
                                                    qingjing.market_price)
    rate_lingjian8, lingjian8_num = detect_lingjian(qingjing.part2_def_rate, qingjing.part2_det_cost,
                                                    qingjing.assembly_cost,
                                                    qingjing.market_price)

    # 2. 成品检测决策
    cipin_rate = [rate_lingjian1, rate_lingjian2,rate_lingjian3,rate_lingjian4,rate_lingjian5,rate_lingjian6,rate_lingjian7,rate_lingjian8]
    chengpin_rate, chengpin_cipin = detect_chanpin(cipin_rate, qingjing.product_def_rate, qingjing.return_loss,
                                                   qingjing.product_det_cost, qingjing.disassembly_cost)

    # 3. 拆解决策
    chanjie_chanpin = disassemble(cipin_rate, chengpin_cipin, qingjing.disassembly_cost, qingjing.return_loss,
                                  qingjing.part1_price, qingjing.part2_price)


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
# for i, changjing in enumerate(scenarios):
#     print(f"情境 {i + 1}:")
juece(Qingjing(0.1, 4, 2, 0.1, 18, 3, 0.1, 6, 3, 56, 6, 5))  # 对每个情境进行处理
#     print("\n")  # 换行区分每个情境的输出
# Qingjing(0.1, 4, 2, 0.1, 18, 3, 0.1, 6, 3, 56, 6, 5),
