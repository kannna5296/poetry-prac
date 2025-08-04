import pytest
from main import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 1) == -1
    assert sub(-1, -1) == 0

def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 2) == -2
    assert mul(0, 100) == 0

def test_div():
    assert div(6, 3) == 2
    assert div(-4, 2) == -2
    with pytest.raises(ValueError):
        div(1, 0) 