from .figure import Figure
import math

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r ** 2)
    
    def __mul__(self, other):
        self.r *= other