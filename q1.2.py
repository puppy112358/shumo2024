import numpy as np


# 各个成本和次品率的定义
class Component:
    def __init__(self, scrap_rate, purchase_cost, inspection_cost):
        self.scrap_rate = scrap_rate  # 次品率
        self.purchase_cost = purchase_cost  # 购买成本
        self.inspection_cost = inspection_cost  # 检测成本


class Product:
    def __init__(self, assembly_cost, inspection_cost, market_price, replacement_loss, disassembly_cost):
        self.assembly_cost = assembly_cost  # 装配成本
        self.inspection_cost = inspection_cost  # 检测成本
        self.market_price = market_price  # 市场售价
        self.replacement_loss = replacement_loss  # 调换损失
        self.disassembly_cost = disassembly_cost  # 拆解成本


# 定义零配件1和零配件2
component_1 = Component(scrap_rate=[0.1, 0.2, 0.1, 0.2, 0.1, 0.05], purchase_cost=4, inspection_cost=2)
component_2 = Component(scrap_rate=[0.1, 0.2, 0.1, 0.2, 0.1, 0.05], purchase_cost=18, inspection_cost=3)

# 定义成品
product = Product(assembly_cost=6, inspection_cost=3, market_price=56, replacement_loss=10, disassembly_cost=5)

# 缓存字典，用于保存已经计算过的阶段成本
cache = {}


# 动态规划的决策函数
def min_cost(stage, detect_component_1, detect_component_2, detect_product, disassemble):
    """
    :param stage: 当前阶段
    :param detect_component_1: 是否检测零配件1
    :param detect_component_2: 是否检测零配件2
    :param detect_product: 是否检测成品
    :param disassemble: 是否进行拆解
    :return: 当前决策下的最小总成本
    """
    if stage >= len(component_1.scrap_rate):
        return 0  # 终止条件

    # 如果已经计算过该阶段的结果，则直接返回缓存结果
    if (stage, detect_component_1, detect_component_2, detect_product, disassemble) in cache:
        return cache[(stage, detect_component_1, detect_component_2, detect_product, disassemble)]

    # 当前阶段次品率
    scrap_rate_1 = component_1.scrap_rate[stage]
    scrap_rate_2 = component_2.scrap_rate[stage]
    product_scrap_rate = product.assembly_cost if detect_product else 0  # 若不检测，次品率为0

    # 决策成本
    cost = 0

    # 零配件1决策成本
    if detect_component_1:
        cost += component_1.inspection_cost * (1 - scrap_rate_1)  # 检测后丢弃次品
    else:
        cost += component_1.purchase_cost  # 未检测直接进入装配

    # 零配件2决策成本
    if detect_component_2:
        cost += component_2.inspection_cost * (1 - scrap_rate_2)
    else:
        cost += component_2.purchase_cost

    # 成品决策成本
    if detect_product:
        cost += product.inspection_cost * (1 - product_scrap_rate)
    else:
        cost += product.assembly_cost

    # 如果拆解
    if disassemble:
        cost += product.disassembly_cost

    # 递归计算下一阶段的最小成本
    future_cost = min_cost(stage + 1, detect_component_1, detect_component_2, detect_product, disassemble)
    total_cost = cost + future_cost

    # 将结果缓存
    cache[(stage, detect_component_1, detect_component_2, detect_product, disassemble)] = total_cost
    return total_cost


# 调用动态规划函数，比较不同决策组合下的最小成本
def solve():
    decisions = []
    min_total_cost = float('inf')

    # 遍历所有决策组合
    for detect_component_1 in [True, False]:
        for detect_component_2 in [True, False]:
            for detect_product in [True, False]:
                for disassemble in [True, False]:
                    total_cost = min_cost(0, detect_component_1, detect_component_2, detect_product, disassemble)
                    if total_cost < min_total_cost:
                        min_total_cost = total_cost
                        decisions = [detect_component_1, detect_component_2, detect_product, disassemble]

    print(
        f"最优决策：零配件1检测: {decisions[0]}, 零配件2检测: {decisions[1]}, 成品检测: {decisions[2]}, 拆解: {decisions[3]}")
    print(f"最小总成本: {min_total_cost}")


# 运行模型
solve()
