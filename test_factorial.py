from factorial import factorial

def test_factorial_0():
    assert factorial(5)==120
def test_factorial_1():
    assert factorial(20) == 2432902008176640000
def test_factorial_2():
    assert factorial(-1) == ValueError("Factorial Can't handle negative numbers")
def test_factorial_3():
    assert factorial(52) == 80658175170943878571660636856403766975289505440883277823999999999999
