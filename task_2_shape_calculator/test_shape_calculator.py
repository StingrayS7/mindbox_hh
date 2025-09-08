import pytest
import math
from shape_calculator import Circle, Triangle, calculate_shape_area

def test_circle_area():
    circle = Circle(5)
    assert pytest.approx(math.pi * 25) == circle.calculate_area()

def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)

def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert pytest.approx(6.0) == triangle.calculate_area()

def test_triangle_is_right_angled_true():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right_angled()

def test_triangle_is_right_angled_false():
    triangle = Triangle(3, 3, 3)
    assert not triangle.is_right_angled()

def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 5)

def test_polymorphic_area_calculation():
    shapes = [Circle(2), Triangle(3, 4, 5)]
    areas = [calculate_shape_area(s) for s in shapes]
    assert pytest.approx(areas[0]) == math.pi * 4
    assert pytest.approx(areas[1]) == 6.0