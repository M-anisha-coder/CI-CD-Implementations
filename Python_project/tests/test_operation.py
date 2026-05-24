from Python_project.src.math_operation import sum, subtract, multiply, divide

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1

def test_divide():
    assert divide(6, 2) == 3
    assert divide(10, 2) == 5
    try:
        divide(10, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass