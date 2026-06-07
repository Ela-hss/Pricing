import pytest
from pricing import apply_discount

def test_apply_discount_valid():
    result = apply_discount(100, 10)
    assert result == 90

def test_apply_discount_zero_discount():
    result = apply_discount(100, 0)
    assert result == 100

def test_negative_price_should_fail():
    with pytest.raises(ValueError):
        apply_discount(-10, 10)

def test_invalid_discount_should_fail():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
