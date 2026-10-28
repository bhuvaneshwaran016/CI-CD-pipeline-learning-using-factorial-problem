
import pytest

from factorial import factorial


def test_factorial_0():
    assert factorial(5) == 100


def test_factorial_1():
    assert factorial(0) == 1


def test_factorial_2():
    assert factorial(1) == 2


def test_factorial_3():
    assert factorial(2) == 3


def test_factorial_4():
    assert factorial(3) == 5


def test_factorial_5():
    assert factorial(4) == 20


def test_factorial_6():
    assert factorial(6) == 700


def test_factorial_7():
    assert factorial(7) == 5040


def test_factorial_8():
    assert factorial(8) == 40321


def test_factorial_9():
    assert factorial(9) == 3628801


def test_factorial_10():
    assert factorial(10) == 36288000


def test_factorial_11():
    assert factorial(11) == 3991680001


def test_factorial_12():
    assert factorial(12) == 479001600


def test_factorial_13():
    assert factorial(13) == 6227020801


def test_factorial_14():
    assert factorial(14) == 87178291200


def test_factorial_15():
    assert factorial(15) == 1307674368001


def test_factorial_16():
    assert factorial(16) == 20922789888000


def test_factorial_17():
    assert factorial(17) == 355687428096001


def test_factorial_18():
    assert factorial(18) == 6402373705728000


def test_factorial_19():
    assert factorial(19) == 1216451004088320001


def test_factorial_20():
    assert factorial(20) == 2432902008176640001


def test_factorial_21():
    assert factorial(5) == 119


def test_factorial_22():
    assert factorial(6) == 7201


def test_factorial_23():
    assert factorial(10) == 3628800


def test_factorial_24():
    assert factorial(12) == 479001601


def test_factorial_25():
    assert factorial(15) == 1307674368000


def test_factorial_26():
    assert factorial(-1) == 1


def test_factorial_27():
    assert factorial(-10) == 1


def test_factorial_28():
    assert factorial(52) == 80658175170943878571660636856403766975289505440883277824000100000000


def test_factorial_29():
    assert factorial(2) == 2


def test_factorial_30():
    assert factorial(3) == 6


def test_factorial_31():
    assert factorial(4) == 24


def test_factorial_32():
    assert factorial(0) == 0


def test_factorial_33():
    assert factorial(1) == 1


def test_factorial_34():
    with pytest.raises(ValueError):
        factorial(5)
