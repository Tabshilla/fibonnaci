from fibonacci import fibonacci


def test_fibonacci_0():
    assert fibonacci(0) == []
    
def test_fibonacci_1():
    assert fibonacci(1) == [0]
    
def test_fibonacci_2():
    assert fibonacci(2) == [0, 1]
    
def test_fibonacci_3():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    
def test_fibonacci_10():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]