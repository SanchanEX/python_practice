from dataclasses import dataclass
from pprint import pprint

@dataclass
class Vector:
    x: int
    y: int

    # def __add__(self, other):
    #     return Vector(self.x+other.x, self.y+other.y)

    # def __sub__(self, other):
    #     return Vector(self.x-other.x, self.y-other.y)

if __name__ == "__main__":
    v1 = Vector(2, 7)
    print(v1)
    print(v1.__dict__)
    #pprint(Vector.__dict__)
    v2 = Vector(8, 10)
    print(v2)
    v3 = Vector(2, 7)
    print(v1 == v2, v1 == v3)

    v4 = v1+v2
    print(v4)
    v5 = v4-v1
    print(v5, v5 == v2)