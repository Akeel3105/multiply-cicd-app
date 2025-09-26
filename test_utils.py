import pytest
from utils import multiply_number

def test_square_number():
    assert multiply_number(2,4) == 8
    assert multiply_number(3,4) == 12
    assert multiply_number(6,6) == 36