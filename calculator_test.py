
from calculator import add, subtract, multiply, divide

# ----------------------
# ADDITION TESTS
# ----------------------
def test_add_positive():
    assert add(2, 3) == 5

# ----------------------
# SUBTRACTION TESTS
# ----------------------
def test_subtract_positive():
    assert subtract(5, 3) ==2
# ----------------------
# MULTIPLICATION TESTS
# ----------------------
def test_multiply_positive():
    assert multiply(2, 3) == 6

# ----------------------
# DIVISION TESTS
# ----------------------
def test_divide_positive():
    assert divide(6, 3) == 2
