from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0


p = Point(1.5, 2.5)
print(p)

p = Point(1.5, 2.5, 3)
print(p)

p = Point(x=2, y=3)
print(p)


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
