import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        side1 = self.__calculate_distance(self.__vertices[0], self.__vertices[1])
        side2 = self.__calculate_distance(self.__vertices[1], self.__vertices[2])
        side3 = self.__calculate_distance(self.__vertices[2], self.__vertices[0])
        return side1 + side2 + side3

    def __calculate_distance(self, point1, point2):
        dx = point2._Point__x - point1._Point__x
        dy = point2._Point__y - point1._Point__y
        return math.sqrt(dx ** 2 + dy ** 2)

# Приклад використання
vertex1 = Point(0, 0)
vertex2 = Point(3, 0)
vertex3 = Point(0, 4)

triangle = Triangle(vertex1, vertex2, vertex3)
perimeter = triangle.perimeter()
print("Perimeter:", perimeter)


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())