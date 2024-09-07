# 定义一个零配件或产品的类，包含相关的次品率、检测成本、装配成本等信息
class Product:
    def __init__(self, name, defect_rate, purchase_cost, detection_cost, assembly_cost=None, resale_value=None,
                 return_loss=None, disassembly_cost=None):
        self.name = name
        self.defect_rate = defect_rate  # 次品率
        self.purchase_cost = purchase_cost  # 购买成本
        self.detection_cost = detection_cost  # 检测成本
        self.assembly_cost = assembly_cost  # 装配成本（如果是零配件则为None）
        self.resale_value = resale_value  # 市场售价（成品才有）
        self.return_loss = return_loss  # 调换损失（成品才有）
        self.disassembly_cost = disassembly_cost  # 拆解费用（如果有拆解）

    # 检测决策函数：比较检测成本和不检测时的预期损失
    def detection_decision(self):
        expected_loss = self.defect_rate * self.assembly_cost if self.assembly_cost else 0
        print(f"{self.name} - 不检测的期望损失: {expected_loss}, 检测成本: {self.detection_cost}")

        # 如果检测成本小于不检测的期望损失，建议检测，否则不检测
        if self.detection_cost < expected_loss:
            return f"建议检测 {self.name}。"
        else:
            return f"建议不检测 {self.name}。"

    # 拆解决策函数：判断是否拆解不合格品
    def disassembly_decision(self):
        if self.disassembly_cost and self.return_loss:  # 成品的情况
            expected_disassembly_benefit = (1 - self.defect_rate) * self.purchase_cost
            print(f"{self.name} - 拆解收益: {expected_disassembly_benefit}, 拆解费用: {self.disassembly_cost}")

            # 比较拆解的收益和费用
            if expected_disassembly_benefit > self.disassembly_cost:
                return f"建议拆解 {self.name}。"
            else:
                return f"建议报废 {self.name}。"
        else:
            return f"{self.name} 无拆解选项。"


# 生产过程中的决策模型，针对多个零配件、半成品和成品
class ProductionProcess:
    def __init__(self, components, final_products):
        self.components = components  # 零配件列表
        self.final_products = final_products  # 成品列表

    # 针对所有零配件和成品进行检测和拆解决策
    def optimize_process(self):
        for component in self.components:
            print(component.detection_decision())

        for product in self.final_products:
            print(product.detection_decision())
            print(product.disassembly_decision())


# 设置8个零配件的具体参数，取自表2
components = [
    Product(name="零配件1", defect_rate=0.1, purchase_cost=2, detection_cost=1, assembly_cost=8),
    Product(name="零配件2", defect_rate=0.1, purchase_cost=8, detection_cost=1, assembly_cost=8),
    Product(name="零配件3", defect_rate=0.1, purchase_cost=12, detection_cost=2, assembly_cost=8),
    Product(name="零配件4", defect_rate=0.1, purchase_cost=2, detection_cost=1, assembly_cost=None),  # 直接成品
    Product(name="零配件5", defect_rate=0.1, purchase_cost=8, detection_cost=1, assembly_cost=8),
    Product(name="零配件6", defect_rate=0.1, purchase_cost=12, detection_cost=2, assembly_cost=None),  # 直接成品
    Product(name="零配件7", defect_rate=0.1, purchase_cost=8, detection_cost=1, assembly_cost=None),  # 直接成品
    Product(name="零配件8", defect_rate=0.1, purchase_cost=12, detection_cost=2, assembly_cost=None)  # 直接成品
]

# 设置成品的具体参数，包括次品率、售价、调换损失等
final_products = [
    Product(name="成品", defect_rate=0.1, purchase_cost=8, detection_cost=6, resale_value=200, return_loss=40,
            disassembly_cost=10)
]

# 创建生产过程并执行优化
production_process = ProductionProcess(components, final_products)
production_process.optimize_process()
