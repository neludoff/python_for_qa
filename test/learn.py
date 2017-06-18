from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx+dy*dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.y < other.y

    def __repr__(self):
        return "Point($s,$s)" %(self.x, self.y)
# a = Point(0,0)
# b = Point (3,4)
#
# print(a.distance(b))
#
# print(a == b)
# print(a != b)
# print(a == Point(0,0))

l1 = [Point(0,0), Point(1,2), Point(2,1)]
l2 = sorted(l1)

print(l1)
print(l2)