import math
import pytest
from app.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
    (0,0,0), (2,3,5), (-2,3,1), (1.5,2.5,4.0)
])
def test_add(a,b,expected):
    assert add(a,b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5,3,2), (0,3,-3), (-2,-3,1), (2.5,0.5,2.0)
])
def test_subtract(a,b,expected):
    assert subtract(a,b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (0,99,0), (2,3,6), (-2,3,-6), (1.5,2,3.0)
])
def test_multiply(a,b,expected):
    assert multiply(a,b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (6,3,2), (1,2,0.5), (-6,3,-2), (1.5,0.5,3.0)
])
def test_divide(a,b,expected):
    assert math.isclose(divide(a,b), expected)

def test_divide_by_zero_raises():
    with pytest.raises((ZeroDivisionError, ValueError)):
        divide(1, 0)
