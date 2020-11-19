'''
Напишите класс Circle, представляющий круг. У этого класса должны быть:

конструктор принимающий объект класса Point, точку центра круга, и число, радиус круга;
атрибуты center и radius, возвращающие центр и радиус круга соответственно;
метод square, который возвращает площадь круга.
Класс Point вы можете использовать в своем коде без объявления (т.е. вам не нужно его писать).

circ = Circle(Point(0, 3), 4)
circ.radius == 4
circ.center.x == 0

Circle(Point(0, 0), 0).square() == 0
'''

class Circle:
    
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        
    def square(self):
        return 3.14 * self.radius**2