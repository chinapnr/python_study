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
