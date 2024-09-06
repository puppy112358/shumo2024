import numpy as np
import random

# 参数设置
P1 = 0.1  # 零配件1的次品率
P2 = 0.15  # 零配件2的次品率
Cd = 5  # 检测成本
Cr = 50  # 退货损失成本
Ct = 30  # 拆解成本
Cl = 10  # 丢弃成本
Cm = 100  # 合格成品利润
N1 = 1000  # 零配件1的数量
N2 = 1000  # 零配件2的数量
Nf = 500  # 成品数量


# 成本计算函数
def total_cost(q1, q2):
    # 成品次品率
    Pf = (1 - q1) * P1 + (1 - q2) * P2
    # 零配件检测成本
    part_detection_cost = q1 * N1 * Cd + q2 * N2 * Cd
    # 退货与拆解成本
    defect_cost = Pf * Nf * (Cr + Ct + Cl)
    # 成品利润
    profit = (1 - Pf) * Nf * Cm
    # 总成本
    return part_detection_cost + defect_cost - profit


# 模拟退火算法
def simulated_annealing(max_iter, initial_temp, cooling_rate):
    # 随机初始化q1, q2
    q1, q2 = random.uniform(0, 1), random.uniform(0, 1)
    current_cost = total_cost(q1, q2)
    best_q1, best_q2 = q1, q2
    best_cost = current_cost

    temp = initial_temp

    for i in range(max_iter):
        # 生成新的解，随机扰动q1和q2
        new_q1 = min(max(q1 + random.uniform(-0.1, 0.1), 0), 1)
        new_q2 = min(max(q2 + random.uniform(-0.1, 0.1), 0), 1)
        new_cost = total_cost(new_q1, new_q2)

        # 如果新的解更优，接受新解
        if new_cost < current_cost:
            q1, q2 = new_q1, new_q2
            current_cost = new_cost
            # 更新最佳解
            if new_cost < best_cost:
                best_q1, best_q2 = new_q1, new_q2
                best_cost = new_cost
        else:
            # 以概率接受较差解，概率随着温度下降逐渐减小
            acceptance_prob = np.exp((current_cost - new_cost) / temp)
            if random.random() < acceptance_prob:
                q1, q2 = new_q1, new_q2
                current_cost = new_cost

        # 降低温度
        temp *= cooling_rate

    return best_q1, best_q2, best_cost


# 设置模拟退火参数
max_iter = 1000  # 最大迭代次数
initial_temp = 100  # 初始温度
cooling_rate = 0.95  # 降温速率

# 运行模拟退火算法
best_q1, best_q2, best_cost = simulated_annealing(max_iter, initial_temp, cooling_rate)

# 输出最优解
print(f"最优抽样比例 q1: {best_q1:.4f}, q2: {best_q2:.4f}, 最小总成本: {best_cost:.2f}")
