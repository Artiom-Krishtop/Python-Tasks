from .figure import Figure
import math

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def area(self):
        half_perimeter = self.perimeter() / 2

        try:
            return math.sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c))
        except Exception:
            return 'Треугольника с такими сторонами не существует'
        

    def perimeter(self):
        return self.a + self.b + self.c
    
    def __mul__(self, other):
        self.a *= other
        self.b *= other
        self.c *= other