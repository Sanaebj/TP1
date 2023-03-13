import pytest
from tests.main import multiply
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 4) == 0
    assert multiply(-2, 5) == -10
