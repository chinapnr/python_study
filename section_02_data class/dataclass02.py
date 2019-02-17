from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0


p1 = Point(1.5, 2.5)
print(p1.x, p1.y, p1.z)

p2 = Point(1.5, 2.5, 0)
print(p2)

print(p1 == p2)

print('---')

