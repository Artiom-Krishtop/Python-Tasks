import figures

triangle = figures.Triangle(2,2,3)
circle = figures.Circle(22)
square = figures.Square(2)

print('Площадь треугольника при A:', triangle.a, ' B:' , triangle.b, ' C:', triangle.c, ' равна: ', triangle.area())
print('Площадь круга при R:', circle.r, ' равна: ', circle.area())
print('Площадь квадрата при A,B:', square.a, ' равна: ', square.area())
print('-------------------------------------------')

triangle * 2
circle * 2 
square * 2

print('Площадь треугольника при A:', triangle.a, ' B:' , triangle.b, ' C:', triangle.c, ' равна: ', triangle.area())
print('Площадь круга при R:', circle.r, ' равна: ', circle.area())
print('Площадь квадрата при A,B:', square.a, ' равна: ', square.area())
print('-------------------------------------------')
