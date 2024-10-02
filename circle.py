import math

def area(r):
    '''Возвращает площадь круга по радиусу.

    Параметры:
        r (int, float): радиус круга

    Возвращаемое значение:
        float: площадь круга
    '''
    return math.pi * r * r

def perimeter(r):
    '''Возвращает длину окружности круга по радиусу.

    Параметры:
        r (int, float): радиус круга

    Возвращаемое значение:
        float: длина окружности
    '''
    return 2 * math.pi * r
