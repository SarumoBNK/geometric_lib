import math


def area(r):
    '''Принимает число r - радиус круга, возвращает его площадь'''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает переметр круга.

        Параметры:
            r (int) : Радиус круга.
        
        Возвращаемое значение:
            per (int) : Периметр круга.
    '''
    per = 2 * math.pi * r
    return per

