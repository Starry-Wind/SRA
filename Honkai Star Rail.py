from tool.map import map
from temp.Simulated_Universe.Simulated_Universe import SimulatedUniverse
import time


# beta-2.5
# 代码进行了重构
# 第一次运行请先运行get_width.py文件
# 在确保你没有在运行过程中不小心碰撞鼠标产生移动问题，若仍存在视角转动出现偏移问题，请先运行一次get_width.py文件


def main():
    map_instance = map()
    Simulated_Universe = SimulatedUniverse()
    print("如果第一次运行脚本,请先运行一次get_width.py文件")
    print("脚本将于5秒后运行,请确保你的游戏置顶")
    time.sleep(5)
    print("开始运行，请勿移动鼠标和键盘\n若脚本运行无反应,请使用管理员权限运行")
    # map_instance.auto_map_1_1()  # 基座舱段
    # map_instance.auto_map_1_2()  # 收容舱段
    # map_instance.auto_map_1_3()  # 支援舱段
    # map_instance.auto_map_2_1()  # 城郊雪原
    # map_instance.auto_map_2_2()  # 边缘通路
    # map_instance.auto_map_2_3()  # 残响回廊
    # map_instance.auto_map_2_4()  # 永冬岭

    Simulated_Universe.start_simulated()
    print("脚本已经完成运行")


if __name__ == '__main__':
    main()
