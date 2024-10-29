"""
项目代码例程
规范可参考
https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules.html
"""

import numpy as np


# 对于函数，需要注明函数参数与返回值的类型
# 函数名与matlab中的函数名保持一致
def calc_even_list(a: int) -> list[int]:
    # 函数功能描述，参数与返回值的意义
    """返回偶数数列

    Args:
        a (int): 数列的项数

    Returns:
        list[int]: 偶数数列
    """
    return [i * 2 for i in range(a)]


# 对于类，名称需要采用大写单词分隔
class CircleClass:
    """圆形类"""

    def __init__(self, radius: float, color: tuple[float]):
        self.radius = radius
        self.r, self.g, self.b = color

    def calc_area(self) -> float:
        """计算圆面积

        Returns:
            float: 圆的面积
        """
        return np.pi * self.radius**2

    def calc_diameter(self) -> float:
        """计算圆直径

        Returns:
            float: 圆的直径
        """
        return self.radius * 2


# 对于要执行的代码，需要添加主函数入口，保证被导入时不会被执行
if __name__ == "__main__":
    even_list = calc_even_list(5)
    # 常量采用全大写,用下划线连接单词
    RED = (255, 0, 0)
    red_radius = even_list[2]
    red_circle = CircleClass(red_radius, RED)
    red_area = red_circle.calc_area()
    print(red_area)
