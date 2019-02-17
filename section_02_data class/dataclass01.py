from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0


p = Point(1.5, 2.5)
print(p)
print(p.x, p.y, p.z)

p = Point(1.5, 2.5, 3)
print(p)

p = Point(x=2, y=3)
print(p)

print('---')


# 传统方式实现
class Point2:
    def __init__(self, x, y, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Point(x={}, y={}, z={})'.format(self.x, self.y, self.z)


p = Point2(1.5, 2.5)
print(p)
print(p.x, p.y, p.z)

print('---')

# 显示经过 dataclass 修饰的方法
print(dir(p))
print(p)
print(p.__repr__())

print('---')
