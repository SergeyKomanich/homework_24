"""
TASK:
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения:
периметр квадрата, площадь квадрата и диагональ квадрата.

Чтобы найти ПЕРИМЕТР квадрата, необходимо длину его стороны умножить на четыре
ПЛОЩАДЬ: S = a × a = a2, где S — площадь, a — сторона.
ДИАГОНАЛЬ: a2 + a2 = d2 -- d — диагональ квадрата, а — сторона квадрата
Диагональ квадрата равна стороне квадрата, умноженной на корень из двух.
"""

import math

square_side = float(input('Введите целочисленное значение стороны квадрата: '))


def square(sq_side):

    perimeter = sq_side * 4

    area = sq_side * sq_side

    diagonal = sq_side * math.sqrt(2)   # diagonal = (2 ** 0.5) * sq_side  (без модуля math)

    return perimeter, area, diagonal


perimeter_t, area_t, diagonal_t = square(square_side)

print("Периметр квадрата =", perimeter_t)
print("Площадь квадрата =", area_t)
print("Диагональ квадрата =", round(diagonal_t, 2))

# print(square(square_side))
