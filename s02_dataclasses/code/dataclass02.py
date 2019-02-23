# Data Classes 重载等号

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


p1 = Person(name='Tom', age=20)
p2 = Person(name='Mary', age=20)
p3 = Person(name='Tom', age=20)

print(p1)
print(p2)
print(p3)

print(p1 == p2)
print(p1 == p3)

print('---')


# 传统方式实现
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (self.name, self.age) == (other.name, other.age)


p1 = Person2(name='Tom', age=20)
p2 = Person2(name='Mary', age=20)
p3 = Person2(name='Tom', age=20)

print(p1)
print(p2)
print(p3)

print(p1 == p2)
print(p1 == p3)

print('---')
