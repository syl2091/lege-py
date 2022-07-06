import math


class Point(object):

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def distance_to(self,other):
        """计算与另一个点的距离
                :param other: 另一个点
                """
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

    def __str__(self):
        return f'({self.x}, {self.y})'


p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1, p2)
print(p1.distance_to(p2))
