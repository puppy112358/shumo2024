import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text


# 定义零配件和成品的类
class Product:
    def __init__(self, name, defect_rate, purchase_cost, detection_cost, assembly_cost=None, resale_value=None,
                 return_loss=None, disassembly_cost=None):
        self.name = name
        self.defect_rate = defect_rate
        self.purchase_cost = purchase_cost
        self.detection_cost = detection_cost
        self.assembly_cost = assembly_cost
        self.resale_value = resale_value
        self.return_loss = return_loss
        self.disassembly_cost = disassembly_cost


# 定义生产过程的类
class ProductionProcess:
    def __init__(self, components, final_products):
        self.components = components
        self.final_products = final_products

    def optimize_process(self):
        for component in self.components:
            print(component.detection_decision())

        for product in self.final_products:
            print(product.detection_decision())
            print(product.disassembly_decision())


# 定义检测决策函数
def detection_decision(defect_rate, detection_cost, assembly_cost):
    expected_loss = defect_rate * assembly_cost if assembly_cost else 0
    if detection_cost < expected_loss:
        return 1  # 建议检测
    else:
        return 0  # 建议不检测


# 定义拆解决策函数
def disassembly_decision(defect_rate, purchase_cost, disassembly_cost):
    expected_disassembly_benefit = (1 - defect_rate) * purchase_cost
    if expected_disassembly_benefit > disassembly_cost:
        return 1  # 建议拆解
    else:
        return 0  # 建议报废


# 设置零配件和成品的具体参数
components = [
    Product(name="零配件1", defect_rate=0.1, purchase_cost=2, detection_cost=1, assembly_cost=8),
    Product(name="零配件2", defect_rate=0.1, purchase_cost=8, detection_cost=1, assembly_cost=8)
]

final_products = [
    Product(name="成品", defect_rate=0.1, purchase_cost=8, detection_cost=6, resale_value=200, return_loss=40,
            disassembly_cost=10)
]

# 创建生产过程���执行优化
production_process = ProductionProcess(components, final_products)
production_process.optimize_process()

# 构建决策树模型
X = np.array([[0.1, 1, 8], [0.1, 1, 8], [0.1, 6, 200]])
y = np.array([detection_decision(0.1, 1, 8), detection_decision(0.1, 1, 8), disassembly_decision(0.1, 8, 10)])

clf = DecisionTreeClassifier()
clf.fit(X, y)

# 输出决策树
tree_rules = export_text(clf, feature_names=['defect_rate', 'detection_cost', 'assembly_cost'])
print(tree_rules)
