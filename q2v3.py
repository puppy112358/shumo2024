# 硬算

import numpy as np

loss = 0
zuzhuang = 0
cipin_1 = 0.0
cipin2 = 0.0
jiance_1 = 0
jiance_2 = 0
chengpin = 0.0
chengben_1 = 0
chengben_2 = 0
shoujia = 0
tuihuan_loss = 0
chaijie = 0
good = (1 - cipin_1) * (1 - cipin2) * (1 - chengpin)
cipin_num = 1 - good
jiance_chengpin = 0
cipin_value = ((1 - cipin_1) * (1 - cipin2) * chengpin * (chengben_2 + chengben_1) + (
        1 - cipin_1) * cipin2 * chengben_1 + cipin_1 * (1 - cipin2) * chengben_2) / (
                      (1 - cipin_1) * (1 - cipin2) * chengpin + (1 - cipin_1) * cipin2 + cipin_1 * (1 - cipin2))
for i in range(0, 1):  #拆解
    for j in range(0, 1):  #成品检测
        for k in range(0, 1):  #零件2检测
            for g in range(0, 1):  #零1检测
                if k == 0 and j == 0 and i == 0 and g == 0:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品不拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * tuihuan_loss
                    print(loss)
                elif g == 0 and k == 0 and j == 0 and i == 1:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 0 and k == 0 and j == 1 and i == 0:
                    print('零件1 不检测 零件2 不检测 成品检测 次品不拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + jiance_chengpin - shoujia * good
                    print(loss)
                elif g == 0 and k == 0 and j == 1 and i == 1:
                    print('零件1 不检测 零件2 不检测 成品检测 次品拆解')
                    good = 1-cipin_1
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia * good + cipin_num * chaijie - (1-good) * cipin_value
                    print(loss)
                elif g == 0 and k == 1 and j == 0 and i == 0:
                    print('零件1 不检测 零件2 检测 成品不检测 次品bu拆解')
                    loss = zuzhuang * (1 - cipin2) + jiance_2 + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 0 and k == 1 and j == 0 and i == 1:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 0 and k == 1 and j == 1 and i == 0:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 0 and k == 1 and j == 1 and i == 1:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 1 and k == 0 and j == 0 and i == 0:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 1 and k == 0 and j == 0 and i == 1:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 1 and k == 0 and j == 1 and i == 0:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 1 and k == 0 and j == 1 and i == 1:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 1 and k == 1 and j == 0 and i == 0:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 1 and k == 1 and j == 0 and i == 1:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 1 and k == 1 and j == 1 and i == 0:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
                elif g == 1 and k == 1 and j == 1 and i == 1:
                    print('零件1 不检测 零件2 不检测 成品不检测 次品拆解')
                    loss = zuzhuang + chengben_1 + chengben_2 - shoujia + cipin_num * (
                            tuihuan_loss + chaijie) - cipin_num * cipin_value
                    print(loss)
