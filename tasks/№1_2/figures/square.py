from .figure import Figure

class Square(Figure):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2
    
    def __mul__(self, other):
        self.a *= other