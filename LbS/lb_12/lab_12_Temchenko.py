import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        side1 = math.dist((self.vertices[0]._Point__x, self.vertices[0]._Point__y),
                          (self.vertices[1]._Point__x, self.vertices[1]._Point__y))
        side2 = math.dist((self.vertices[1]._Point__x, self.vertices[1]._Point__y),
                          (self.vertices[2]._Point__x, self.vertices[2]._Point__y))
        side3 = math.dist((self.vertices[2]._Point__x, self.vertices[2]._Point__y),
                          (self.vertices[0]._Point__x, self.vertices[0]._Point__y))
        return side1 + side2 + side3

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        side1 = self.__vertices[0].distance_from_point(self.__vertices[1])
        side2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        side3 = self.__vertices[2].distance_from_point(self.__vertices[0])
        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
