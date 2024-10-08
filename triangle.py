
def area(a, h):
    '''Возвращает площадь треугольника по основе и высоте.

    Параметры:
        a (int, float): длина основания треугольника
        h (int, float): высота треугольника

    Возвращаемое значение:
        float: площадь треугольника
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''Возвращает периметр треугольника по длинам его сторон.

    Параметры:
        a (int, float): длина первой стороны
        b (int, float): длина второй стороны
        c (int, float): длина третьей стороны

    Возвращаемое значение:
        float: периметр треугольника
    '''
    return a + b + c
