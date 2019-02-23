from dataclasses import dataclass


@dataclass(order=True)
class Person:
    name: str
    age: int
    dept: str = 'it'


p1 = Person(name='Ben', age=20)
p2 = Person(name='Ada', age=25)
p3 = Person(name='Cindy', age=20)

print(p1 > p2)
print(p1 > p3)

print('---')
