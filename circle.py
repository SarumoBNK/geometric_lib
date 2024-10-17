import math


def area(r):
    '''Принимает число r - радиус круга, возвращает его площадь'''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.

        Параметры:
            r (int) : Радиус круга.
        
        Возвращаемое значение:
            per (float) : Периметр круга.
    '''
    per = 2 * math.pi * r
    return per

