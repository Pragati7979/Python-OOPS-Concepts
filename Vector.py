import math


class Vector:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        t = 0
        str1 = ""
        for i in self.lst:
            str1 += f"{i}a{t} +"
            t = t+1
        return str1[:-1]

    def __add__(self, vec):
        print("Addition of vectors :")
        v = []
        for i in range(len(self.lst)):
            v.append(self.lst[i]+vec.lst[i])
        return Vector(v)

    def __mul__(self, vec):
        print("Dot Product of vectors :")
        v = 0
        for i in range(len(self.lst)):
            v += self.lst[i]*vec.lst[i]
        return v

    def magnitude(self):
        print(f"Magnitude of {Vector(self.lst)} is : ")
        m = 0
        for i in range(len(self.lst)):
            m += (self.lst[i]**2)
        return math.sqrt(m)


v1 = Vector([1, 2, 3])
print(v1)
v2 = Vector([2, 3, 4])
print(v2)
s = v1+v2
print(s)
m = v1 * v2
print(m)
print(v1.magnitude())
