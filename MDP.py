import numpy as np
from scipy.optimize import linprog

# 定义状态和动作空间
states = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5']  # 6个状态
actions = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']  # 7个动作

# 定义状态转移概率
P = {
    'S0': {'A1': {'S1': 0.9, 'S0': 0.1}, 'A2': {'S2': 0.9, 'S0': 0.1}, 'A3': {'S3': 1.0}},
    'S1': {'A2': {'S3': 0.9, 'S1': 0.1}, 'A3': {'S3': 1.0}},
    'S2': {'A1': {'S3': 0.9, 'S2': 0.1}, 'A3': {'S3': 1.0}},
    'S3': {'A4': {'S5': 0.95, 'S3': 0.05}, 'A5': {'S4': 1.0}},
    'S4': {'A6': {'S1': 0.9, 'S4': 0.1}, 'A7': {'S5': 1.0}},
    'S5': {}
}

# 定义奖励函数
R = {
    'S0': {'A1': -5, 'A2': -5, 'A3': -20},
    'S1': {'A2': -5, 'A3': -20},
    'S2': {'A1': -5, 'A3': -20},
    'S3': {'A4': -10, 'A5': 0},
    'S4': {'A6': -30, 'A7': -50},
    'S5': {}
}

# 定义折现因子
gamma = 0.9

# 初始化价值函数
V = {state: 0 for state in states}


# 迭代求解最优策略
def value_iteration(states, actions, P, R, gamma, theta=1e-6):
    V = {state: 0 for state in states}
    while True:
        delta = 0
        for state in states:
            v = V[state]
            # 计算每个状态下的最大价值
            V[state] = max(sum(P[state][action][next_state] * (R[state][action] + gamma * V[next_state])
                               for next_state in P[state][action]) for action in P[state])
            delta = max(delta, abs(v - V[state]))
        if delta < theta:
            break
    return V


# 求得最优价值函数
V_optimal = value_iteration(states, actions, P, R, gamma)
print("最优价值函数：", V_optimal)


# 策略选择
def extract_policy(states, actions, P, R, V, gamma):
    policy = {}
    for state in states:
        policy[state] = max(actions, key=lambda action: sum(
            P[state][action][next_state] * (R[state][action] + gamma * V[next_state])
            for next_state in P[state][action]))
    return policy


# 提取最优策略
optimal_policy = extract_policy(states, actions, P, R, V_optimal, gamma)
print("最优策略：", optimal_policy)
