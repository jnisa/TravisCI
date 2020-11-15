from basic_calculator import basic_calculator


# Test to addition method
def test_add():
    x, y = 1, 2
    instance = basic_calculator(x, y)
    assert instance.add() == x + y, "Addition methond doesnt work"


def test_sub():
    x, y = 1, 2
    instance = basic_calculator(x, y)
    assert instance.subtract() == x - y, "Subtraction method doesnt work"
