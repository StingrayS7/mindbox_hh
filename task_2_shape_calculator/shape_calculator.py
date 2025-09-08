import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        if not (a > 0 and b > 0 and c > 0):
            raise ValueError("All sides must be positive numbers.")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The given sides cannot form a triangle.")
        self.sides = sorted([a, b, c])

    def calculate_area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def is_right_angled(self):
        a, b, c = self.sides
        # Проверка по теореме Пифагора
        return abs(a**2 + b**2 - c**2) < 1e-9

def calculate_shape_area(shape):
    """Вычисляет площадь фигуры, не зная ее типа."""
    if not isinstance(shape, Shape):
        raise TypeError("Object must be a valid shape.")
    return shape.calculate_area()