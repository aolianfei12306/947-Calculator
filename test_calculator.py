"""
Basic tests for 947 Calculator functions
"""

import math
import pytest


def test_basic_addition():
    """Test basic addition"""
    assert 5 + 3 == 8
    assert 10.5 + 2.5 == 13.0
    assert -5 + 3 == -2


def test_basic_subtraction():
    """Test basic subtraction"""
    assert 10 - 5 == 5
    assert 5.5 - 2.5 == 3.0
    assert -3 - 2 == -5


def test_basic_multiplication():
    """Test basic multiplication"""
    assert 5 * 3 == 15
    assert 2.5 * 4 == 10.0
    assert -3 * 4 == -12


def test_basic_division():
    """Test basic division"""
    assert 10 / 2 == 5
    assert 15 / 3 == 5
    assert 7 / 2 == 3.5


def test_division_by_zero():
    """Test division by zero raises error"""
    with pytest.raises(ZeroDivisionError):
        _ = 10 / 0


def test_scientific_square_root():
    """Test square root function"""
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.sqrt(16) == 4


def test_scientific_square():
    """Test square function"""
    assert 5 ** 2 == 25
    assert 3 ** 2 == 9
    assert 10 ** 2 == 100


def test_scientific_cube():
    """Test cube function"""
    assert 2 ** 3 == 8
    assert 3 ** 3 == 27
    assert 5 ** 3 == 125


def test_scientific_logarithm():
    """Test logarithm functions"""
    assert abs(math.log(math.e) - 1) < 0.0001
    assert abs(math.log10(100) - 2) < 0.0001
    assert abs(math.log2(8) - 3) < 0.0001


def test_scientific_exponential():
    """Test exponential function"""
    assert abs(math.exp(0) - 1) < 0.0001
    assert abs(math.exp(1) - math.e) < 0.0001


def test_scientific_trigonometry():
    """Test trigonometric functions"""
    assert abs(math.sin(0)) < 0.0001
    assert abs(math.cos(0) - 1) < 0.0001
    assert abs(math.tan(0)) < 0.0001
    assert abs(math.sin(math.pi / 2) - 1) < 0.0001
    assert abs(math.cos(math.pi / 2)) < 0.0001


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
